import json

class DataSaver:
    
    def __init__(self):
        pass

    def make_response_file(self, response_data):
        with open("Data/input.txt", "w", encoding="utf-8") as file:
            json.dump(response_data, file, ensure_ascii=False, indent=2)