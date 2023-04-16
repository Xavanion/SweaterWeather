import json

class Read:
    def __init__(self, file_name):
        self.file = file_name

    def history(self):
        pass

    def run(self):
        global json_data
        with open(self.file) as f:
            json_data = json.load(f)
        


read_stuff = Read('history.json')
