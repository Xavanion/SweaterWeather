import json

class Read:
    def __init__(self, file_name):
        self.file = file_name

    def history(self):
        location_data = {}
        location_data['country'] = json_data['location']['country']
        location_data['city'] = json_data['location']['name']

        monthly_data_json = json_data['forecast']['forecastday']
        monthly_data = {}
        monthly_data['location'] = location_data
        i = 1
        for forecastday in monthly_data_json:
            date = forecastday['_date']

            tempinfo = {}
            tempinfo['mintemp'] = forecastday['day']['mintemp_f']
            tempinfo['maxtemp'] = forecastday['day']['maxtemp_f']
            tempinfo['avgtemp'] = forecastday['day']['avgtemp_f']

            conditioninfo = {}
            conditioninfo['icon'] = forecastday['day']['condition']['icon']
            conditioninfo['condition'] = forecastday['day']['condition']['text']

            hourinfo = {}
            hourinfo['date'] = date
            hourinfo['temperature'] = tempinfo
            hourinfo['condition'] = conditioninfo

            monthly_data[f'Day {i}'] = hourinfo
            i += 1
        return monthly_data

    def realtime(self):
        realtimedata = {}

        location_data = {}
        location_data['country'] = json_data['location']['country']
        location_data['city'] = json_data['location']['name']
        realtimedata['location'] = location_data

        currentdata = json_data['current']
        
        conditioninfo = {}
        conditioninfo['icon'] = currentdata['condition']['icon']
        conditioninfo['condition'] = currentdata['condition']['icon']
        realtimedata['condition'] = conditioninfo

        tempinfo = {}
        tempinfo['temp'] = currentdata['temp_f']
        tempinfo['feelslike'] = currentdata['feelslike_f']
        realtimedata['temperature'] = tempinfo

        return realtimedata 
    
    def forecast(self):
        daily_forecast = {}
        alldayforecast = json_data['forecast']['forecastday'][0]['hour']
        date = json_data['forecast']['forecastday'][0]['_date']

        location_data = {}
        location_data['country'] = json_data['location']['country']
        location_data['city'] = json_data['location']['name']
        daily_forecast['location'] = location_data

        i = 1
        for hourlydata in alldayforecast:
            times = ["00:00", "06:00", "12:00", "18:00", "23:00"]
            time = str(hourlydata['time'][11:])
            if time in times:
                hourinfo = {}

                dateinfo = {}
                dateinfo['date'] = date
                dateinfo['time'] = time
                hourinfo['date_and_time'] = dateinfo

                info = {}
                info['temperature'] = hourlydata['temp_f']
                info['feelslike'] = hourlydata['feelslike_f']
                info['wind_speed'] = hourlydata['wind_mph']
                info['chance_of_rain'] = hourlydata['chance_of_rain']
                info['chance_of_snow'] = hourlydata['chance_of_snow']

                
                conditioninfo = {}
                conditioninfo['icon'] = hourlydata['condition']['icon']
                conditioninfo['condition'] = hourlydata['condition']['text']

                hourinfo['info'] = info
                hourinfo['conditioninfo'] = conditioninfo
            daily_forecast[f'time_interval{i}'] = hourinfo
            i += 1
        return daily_forecast
        

    def run(self):
        global json_data
        with open(self.file) as f:
            json_data = json.load(f)
        print(self.forecast())


read_stuff = Read('forecast.json')
read_stuff.run()
