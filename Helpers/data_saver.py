import json

if __name__ == "__main__":
    raise Exception("Нужно запускать wb_parser.py")

class DataSaver:
    
    def __init__(self):
        pass

    def make_response_file(self, response_data):
        with open("Data/input.txt", "w", encoding="utf-8") as file:
            json.dump(response_data, file, ensure_ascii=False, indent=2)
    
    def save_xlsx(self, rows: list[dict], output_path: str):
        pass