from __future__ import print_function
from swagger_client.rest import ApiException
from pprint import pprint
import time, geocoder, swagger_client, json, flask, sqlite3


# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['key'] = ''

#Location Stoof
g = geocoder.ip('me')
cur_location = [str(x) for x in g.latlng]
cur_location = ','.join(cur_location)


def search():
    # create an instance of the API class
    location = input('Enter a place: ')
    api_instance = swagger_client.APIsApi(swagger_client.ApiClient(configuration))
    q = location # str | Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more. 

    try:
        # Search/Autocomplete API
        api_response = api_instance.search_autocomplete_weather(q)
        #data = api_response.to_dict()
        print(api_response)
        print(type(api_response))
        #with open('search.json', 'w') as f:
        #    f.write(json.dumps(data, indent=4, sort_keys=True, default=str))
        #pprint(api_response)
    except ApiException as e:
        print("Exception when calling APIsApi->search_autocomplete_weather: %s\n" % e)

def real_time(location):
    # create an instance of the API class
    api_instance = swagger_client.APIsApi(swagger_client.ApiClient(configuration))
    q = location # str | Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more. 
    
    try:
        # Realtime API
        api_response = api_instance.realtime_weather(q)
        data = api_response.to_dict()
        with open('real_time.json', 'w') as f:
            f.write(json.dumps(data, indent=4, sort_keys=True, default=str))
        #pprint(api_response)
    except ApiException as e:
        print("Exception when calling APIsApi->realtime_weather: %s\n" % e)

def future(location):
    # create an instance of the API class
    api_instance = swagger_client.APIsApi(swagger_client.ApiClient(configuration))
    q = location # str | Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more. 
    dt = '2023-06-20' # date | Date should be between today and next 14 day in yyyy-MM-dd format. e.g. '2015-01-01'  (optional)

    try:
        # Future API dt is 14-300 days in the future
        api_response = api_instance.future_weather(q, dt=dt)
        data = api_response.to_dict()
        with open('future.json', 'w') as f:
            f.write(json.dumps(data, indent=4, sort_keys=True, default=str))
        #pprint(api_response)
    except ApiException as e:
        print("Exception when calling APIsApi->future_weather: %s\n" % e)



def history(location):
    # create an instance of the API class
    api_instance = swagger_client.APIsApi(swagger_client.ApiClient(configuration))
    q = location # str | Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more. 
    dt = '2023-01-01' # date | Date on or after 1st Jan, 2015 in yyyy-MM-dd format
    end_dt = '2023-01-30' # date | Date on or after 1st Jan, 2015 in yyyy-MM-dd format<br />'end_dt' should be greater than 'dt' parameter and difference should not be more than 30 days between the two dates.  (optional)
    hour = 12 # int | Must be in 24 hour. For example 5 pm should be hour=17, 6 am as hour=6  (optional)

    try:
        # History API
        api_response = api_instance.history_weather(q, dt, end_dt=end_dt, hour=hour)
        data = api_response.to_dict()
        with open('history.json', 'w') as f:
            f.write(json.dumps(data, indent=4, sort_keys=True, default=str))
        #pprint(api_response)
    except ApiException as e:
        print("Exception when calling APIsApi->history_weather: %s\n" % e)


def forecast(location):
    # create an instance of the API class
    api_instance = swagger_client.APIsApi(swagger_client.ApiClient(configuration))
    q = location # str | Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more. 
    days = 7 # int | Number of days of weather forecast. Value ranges from 1 to 14
    dt = '2023-04-20' # date | Date should be between today and next 14 day in yyyy-MM-dd format. e.g. '2015-01-01'  (optional)
    hour = 12 # int | Must be in 24 hour. For example 5 pm should be hour=17, 6 am as hour=6  (optional)

    try:
        # Forecast API
        api_response = api_instance.forecast_weather(q, days, dt=dt, hour=hour)
        data = api_response.to_dict()
        with open('forecast.json', 'w') as f:
            f.write(json.dumps(data, indent=4, sort_keys=True, default=str))
        #pprint(api_response)
    except ApiException as e:
        print("Exception when calling APIsApi->forecast_weather: %s\n" % e)

def site():
    # Make Flask App
    app = flask.Flask(__name__)
    @app.route('/', methods=['GET', 'POST'])
    def index():
        # Takes form method post with name city and sets that equal to city name
        # Thinking of passing cityname to insert_record for sql database for later email list/recommendations
        if flask.request.method == "POST":
            radio_choice = flask.request.form.get("radioChoice")
            if radio_choice == 'CurrentData':
                print("Current")
            elif radio_choice == 'PastData':
                print("Past")
            elif radio_choice == 'Forecast':
                print("Forecast")
            if (city_name:=flask.request.form['location']):
                real_time(city_name)
        # Command to render site (Has to be in a templates folder or we can figure out how to change that if needed)
        return flask.render_template("index.html")

    app.run(debug=True)


def main():
    # Create SQL Datadase
    #conn = sqlite3.connect('email_database.db')
    #c = conn.cursor()
    #c.execute("""CREATE TABLE emails()""")

    site()

    '''
    forecast(cur_location)
    history(cur_location)
    future(cur_location)
    real_time(cur_location)
    search()
    '''


if __name__ == "__main__":
    main()