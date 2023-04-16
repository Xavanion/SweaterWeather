from __future__ import print_function
from swagger_client.rest import ApiException
from pprint import pprint
import geocoder, swagger_client, json, flask, sqlite3, datetime, googlemaps, requests, random
from geopy.geocoders import Nominatim
from read_json import Read


# Lat/Long boi
geolocator = Nominatim(user_agent="Myapp")

#Google maps client
gmaps = googlemaps.Client(key="")

# Flask app
app = flask.Flask(__name__)

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['key'] = ''

#Location Stoof
g = geocoder.ip('me')
cur_location = [str(x) for x in g.latlng]
cur_location = ','.join(cur_location)

location = cur_location

# Time thing
today = datetime.date.today()

# Json file reader
def file_reader(file_name):
    reader = Read(file_name)
    return reader.run()

# API Search call
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
    except ApiException as e:
        print("Exception when calling APIsApi->search_autocomplete_weather: %s\n" % e)

# API Real_time call
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
    except ApiException as e:
        print("Exception when calling APIsApi->realtime_weather: %s\n" % e)

# API future date call
def future(location, date):
    # create an instance of the API class
    api_instance = swagger_client.APIsApi(swagger_client.ApiClient(configuration))
    q = location # str | Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more. 
    dt = date # date | Date should be between today and next 14 day in yyyy-MM-dd format. e.g. '2015-01-01'  (optional)

    try:
        # Future API dt is 14-300 days in the future
        api_response = api_instance.future_weather(q, dt=dt)
        data = api_response.to_dict()
        with open('future.json', 'w') as f:
            f.write(json.dumps(data, indent=4, sort_keys=True, default=str))
    except ApiException as e:
        print("Exception when calling APIsApi->future_weather: %s\n" % e)

# API past history call
def history(location, date):
    # Creates start/end date for API class
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    if (date + datetime.timedelta(days=30)) > today:
        date_end = today - datetime.timedelta(days=1)
    else:
        date_end = date + datetime.timedelta(days=30)
    date = str(date)
    date_end = str(date_end)

    # create an instance of the API class
    api_instance = swagger_client.APIsApi(swagger_client.ApiClient(configuration))
    q = location # str | Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more. 
    dt = date # date | Date on or after 1st Jan, 2015 in yyyy-MM-dd format
    end_dt = date_end # date | Date on or after 1st Jan, 2015 in yyyy-MM-dd format<br />'end_dt' should be greater than 'dt' parameter and difference should not be more than 30 days between the two dates.  (optional)

    try:
        # History API
        api_response = api_instance.history_weather(q, dt, end_dt=end_dt)
        data = api_response.to_dict()
        with open('history.json', 'w') as f:
            f.write(json.dumps(data, indent=4, sort_keys=True, default=str))
    except ApiException as e:
        print("Exception when calling APIsApi->history_weather: %s\n" % e)

# API hourly forecast call
def forecast(location):
    # create an instance of the API class
    api_instance = swagger_client.APIsApi(swagger_client.ApiClient(configuration))
    q = location # str | Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more. 
    days = 7 # int | Number of days of weather forecast. Value ranges from 1 to 14
    dt = '2023-04-20' # date | Date should be between today and next 14 day in yyyy-MM-dd format. e.g. '2015-01-01'  (optional)
    #hour = 12 # int | Must be in 24 hour. For example 5 pm should be hour=17, 6 am as hour=6  (optional)

    try:
        # Forecast API
        api_response = api_instance.forecast_weather(q, days, dt=dt)
        data = api_response.to_dict()
        with open('forecast.json', 'w') as f:
            f.write(json.dumps(data, indent=4, sort_keys=True, default=str))
    except ApiException as e:
        print("Exception when calling APIsApi->forecast_weather: %s\n" % e)

# Run's flask site
def site():
    app.run(debug=True)

# Render's the site when asking for real-time data
def real_time_render(current_info, pizza_pizza):
    choices = random.sample(pizza_pizza['locations'], 3)
    return flask.render_template("index.html", today = str(today), future_min= str(today +  + datetime.timedelta(days=14)), future_max= str(today + datetime.timedelta(days=300)),
                                current_temp = current_info['temperature']['temp'], feels_temp = current_info['temperature']['feelslike'], photo = (current_info['condition']['condition']) + '.png',
                                local = (current_info['location']['city'] + ', ' + current_info['location']['country']), location1=choices[0], location2=choices[1],
                                location3=choices[2], descriptor = (current_info['condition']['condition']), wind_speed = current_info['condition']['windspeed'])

# Handles Default loading of Site
@app.route('/', methods=['GET', 'POST'])
def index():
    real_time(cur_location)
    current_info = file_reader('real_time.json')
    if flask.request.method == "POST":
        radio_choice = flask.request.form.get("radioChoice")
        if radio_choice == 'PastData':
            history(location, flask.request.form.get("PastDate"))
            return flask.send_file('history.json', as_attachment=True, attachment_filename=(flask.request.form.get('PastDate') + "-" + current_info['location']['city'] + '-history.json'))
        elif radio_choice == 'FutureData':
            future(location, flask.request.form.get("FutureDate"))
            return flask.send_file('future.json', as_attachment=True, attachment_filename=(flask.request.form.get('FutureDate') + "-" + current_info['location']['city'] + '-future.json'))
        elif (city_name:=flask.request.form['location']):
            real_time(city_name)
            return flask.redirect(flask.url_for('real_time_data', variable=city_name))
    # Command to render site
    pizza_pizza = pizza_recommender((current_info['location']['city'] + ', ' + current_info['location']['country']))
    return real_time_render(current_info, pizza_pizza)

# View real time data
@app.route('/<variable>/real_time_data', methods=['GET', 'POST'])
def real_time_data(variable):
    real_time(variable)
    current_info = file_reader('real_time.json')
    if flask.request.method == "POST":
        radio_choice = flask.request.form.get("radioChoice")
        if radio_choice == 'PastData':
            history(location, flask.request.form.get("PastDate"))
            return flask.send_file('history.json', as_attachment=True, attachment_filename=(flask.request.form.get('PastDate') + "-" + current_info['location']['city'] + '-history.json'))
        elif radio_choice == 'FutureData':
            future(location, flask.request.form.get("FutureDate"))
            return flask.send_file('future.json', as_attachment=True, attachment_filename=(flask.request.form.get('FutureDate')+ "-" + current_info['location']['city'] + '-future.json'))
        elif (city_name:=flask.request.form['location']):
            real_time(city_name)
            return flask.redirect(flask.url_for('real_time_data', variable=city_name))
    pizza_pizza = pizza_recommender((current_info['location']['city'] + ', ' + current_info['location']['country']))
    return real_time_render(current_info, pizza_pizza)

def pizza_recommender(local):
    geo_location = geolocator.geocode(local)
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=pizza%20restaurants&location="+ str(geo_location.latitude) + "%2C" + str(geo_location.longitude) + "&radius=700&key="
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    with open('recommendations.json', "w", encoding='utf-8') as file:
        file.write(response.text)
    pizza_dict = file_reader('recommendations.json')
    return pizza_dict

def main():
    site()


if __name__ == "__main__":
    main()




# Scary code for later
'''
# Post Request Handler
radio_choice = flask.request.form.get("radioChoice")
if radio_choice == 'PastData':
    history(location, flask.request.form.get("PastDate"))
    return flask.redirect(flask.url_for('past_history', current_info=current_info))
elif radio_choice == 'FutureData':
    future(location, flask.request.form.get("FutureDate"))
    return flask.redirect(flask.url_for('future_history', current_info=current_info, local=(current_info['location']['city'])))

# Render Pages w/Future Requests
def future_render(future_data):
    return flask.render_template("future.html", date = future_data['time_interval1']['date_and_time']['date'], temp = future_data['time_interval1']['info']['temperature'],
                                 feels = future_data['time_interval1']['info']['feelslike'], local = 'Test')

# Render Pages w/Past Requests
def past_render(current_info):
    pass

# View past history of location
@app.route('/city/past_history', methods=['GET', 'POST'])
def past_history(current_info):
    current_info = file_reader('history.json')
    if flask.request.method == 'POST':
        if (city_name:=flask.request.form['location']):
            real_time(city_name)
        return flask.redirect(flask.url_for('real_time_data', variable=city_name))
    

# Viewing Future Data for a given location
@app.route('/<local>/future_history', methods=['GET', 'POST'])
def future_history(current_info, local):
    future(local)
    current_info = file_reader('future.json')
    if flask.request.method == 'POST':
        radio_choice = flask.request.form.get("radioChoice")
        if radio_choice == 'PastData':
            history(location, flask.request.form.get("PastDate"))
            return flask.redirect(flask.url_for('past_history'))
        elif radio_choice == 'FutureData':
            future(location, flask.request.form.get("FutureDate"))
            return flask.redirect(flask.url_for('future_history'))
        elif (city_name:=flask.request.form['location']):
            real_time(city_name)
        return flask.redirect(flask.url_for('real_time_data', variable=city_name))
    return future_render(current_info)

# View Hourly forecast for a location
@app.route('/<variable>/forecast', methods=['GET', 'POST'])
def forecast_call(location):
    pass
'''