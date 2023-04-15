from __future__ import print_function
import time
import geocoder
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


#Location Stoof
g = geocoder.ip('me')
cur_location = [str(x) for x in g.latlng]
cur_location = ','.join(cur_location)

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['key'] = ''
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.APIsApi(swagger_client.ApiClient(configuration))
q = cur_location # str | Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more. 
days = 56 # int | Number of days of weather forecast. Value ranges from 1 to 14
dt = '2013-10-20' # date | Date should be between today and next 14 day in yyyy-MM-dd format. e.g. '2015-01-01'  (optional)
unixdt = 56 # int | Please either pass 'dt' or 'unixdt' and not both in same request. unixdt should be between today and next 14 day in Unix format. e.g. 1490227200  (optional)
hour = 56 # int | Must be in 24 hour. For example 5 pm should be hour=17, 6 am as hour=6  (optional)
lang = 'lang_example' # str | Returns 'condition:text' field in API in the desired language.<br /> Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to check 'lang-code'.  (optional)

try:
    # Forecast API
    api_response = api_instance.forecast_weather(q, days, dt=dt, unixdt=unixdt, hour=hour, lang=lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIsApi->forecast_weather: %s\n" % e)


'''
# create an instance of the API class
api_instance = swagger_client.APIsApi(swagger_client.ApiClient(configuration))
q = 'q_example' # str | Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more. 
dt = '2013-10-20' # date | Date should be between 14 days and 300 days from today in the future in yyyy-MM-dd format (i.e. dt=2023-01-01)  (optional)
lang = 'lang_example' # str | Returns 'condition:text' field in API in the desired language.<br /> Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to check 'lang-code'.  (optional)

try:
    # Future API
    api_response = api_instance.future_weather(q, dt=dt, lang=lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIsApi->future_weather: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.APIsApi(swagger_client.ApiClient(configuration))
q = 'q_example' # str | Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more. 
dt = '2013-10-20' # date | Date on or after 1st Jan, 2015 in yyyy-MM-dd format
unixdt = 56 # int | Please either pass 'dt' or 'unixdt' and not both in same request.<br />unixdt should be on or after 1st Jan, 2015 in Unix format  (optional)
end_dt = '2013-10-20' # date | Date on or after 1st Jan, 2015 in yyyy-MM-dd format<br />'end_dt' should be greater than 'dt' parameter and difference should not be more than 30 days between the two dates.  (optional)
unixend_dt = 56 # int | Date on or after 1st Jan, 2015 in Unix Timestamp format<br />unixend_dt has same restriction as 'end_dt' parameter. Please either pass 'end_dt' or 'unixend_dt' and not both in same request. e.g. unixend_dt=1490227200  (optional)
hour = 56 # int | Must be in 24 hour. For example 5 pm should be hour=17, 6 am as hour=6  (optional)
lang = 'lang_example' # str | Returns 'condition:text' field in API in the desired language.<br /> Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to check 'lang-code'.  (optional)

try:
    # History API
    api_response = api_instance.history_weather(q, dt, unixdt=unixdt, end_dt=end_dt, unixend_dt=unixend_dt, hour=hour, lang=lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIsApi->history_weather: %s\n" % e)


# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['key'] = ''
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.APIsApi(swagger_client.ApiClient(configuration))
q = 'q_example' # str | Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more. 
lang = 'lang_example' # str | Returns 'condition:text' field in API in the desired language.<br /> Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to check 'lang-code'.  (optional)

try:
    # Realtime API
    api_response = api_instance.realtime_weather(q, lang=lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIsApi->realtime_weather: %s\n" % e)

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['key'] = ''
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.APIsApi(swagger_client.ApiClient(configuration))
q = 'q_example' # str | Pass US Zipcode, UK Postcode, Canada Postalcode, IP address, Latitude/Longitude (decimal degree) or city name. Visit [request parameter section](https://www.weatherapi.com/docs/#intro-request) to learn more. 

try:
    # Search/Autocomplete API
    api_response = api_instance.search_autocomplete_weather(q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIsApi->search_autocomplete_weather: %s\n" % e)

'''
