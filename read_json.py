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

            dayinfo = {}
            dayinfo['date'] = date
<<<<<<< Updated upstream
            dayinfo['temperature'] = tempinfo
=======
            dayinfo['temperatures'] = tempinfo
>>>>>>> Stashed changes
            dayinfo['condition'] = conditioninfo

            monthly_data[f'Day {i}'] = dayinfo
            i += 1
<<<<<<< Updated upstream
        return monthly_data

    def realtime(self):
        realtimedata = {}

        location_data = {}
        location_data['country'] = json_data['location']['country']
        location_data['city'] = json_data['location']['name']

        currentdata = json_data['current']
        
        conditioninfo = {}
        conditioninfo['icon'] = currentdata['condition']['icon']
        conditioninfo['condition'] = currentdata['condition']['icon']
        realtimedata['condition'] = conditioninfo

        tempinfo = {}
        tempinfo['temp'] = currentdata['temp_f']
        tempinfo['feelslike'] = currentdata['feelslike_f']
        realtimedata['temperature'] = tempinfo

        print(realtimedata)
=======
        return monthly_data     
        
>>>>>>> Stashed changes

    def run(self):
        global json_data
        with open(self.file) as f:
            json_data = json.load(f)
<<<<<<< Updated upstream
        self.realtime()

read_stuff = Read('real_time.json')
=======
        

read_stuff = Read('history.json')
>>>>>>> Stashed changes

read_stuff.run()
