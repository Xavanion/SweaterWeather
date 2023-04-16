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
            dayinfo['temperatures'] = tempinfo
            dayinfo['condition'] = conditioninfo

            monthly_data[f'Day {i}'] = dayinfo
            i += 1
        return monthly_data     
        

    def run(self):
        global json_data
        with open(self.file) as f:
            json_data = json.load(f)
        

read_stuff = Read('history.json')

read_stuff.run()
