import requests
import json

import Data.data_classes as data_classes

class DataLoader:

    def __init__(self, load_from_file = False, dest: int = -3115289):
        self.dest = dest
        self.load_from_file = load_from_file

    def load_data(self) -> list[dict]:
        if self.load_from_file:
            with open(file="Data/input.txt") as file:
                response_data = json.loads(file.read())

            return response_data['products']
        else:
            request_data = self.__make_request_data(token=self.__get_token())
            return self.__make_request(
                params=request_data.params, 
                cookies=request_data.cookies
            )  

    def __get_token(self) -> str:
        try:
            with open("Data/token.txt") as file:
                return file.readline()
        except:
            raise Exception("" \
                "Невозможно получить токен из файла Data/request_data.txt. " \
                "Проверьте содержимое или наличие файла"
            )
    
    def __make_request_data(self, token: str) -> data_classes.RequestData:
        cookies = {
            'x_wbaas_token': token,
        }

        params = {
            'ab_testing': 'false',
            'appType': '1',
            'curr': 'rub',
            'dest': self.dest,
            'inheritFilters': 'false',
            'lang': 'ru',
            'query': 'пальто из натуральной шерсти',
            'resultset': 'catalog',
            'sort': 'popular',
            'spp': '30',
            'suppressSpellcheck': 'false',
        }

        return data_classes.RequestData(cookies=cookies, params=params)
    
    def __make_request(self, params: dict, cookies: dict):
        response = requests.get(
            'https://www.wildberries.ru/__internal/u-search/exactmatch/ru/common/v18/search',
            params=params,
            cookies=cookies
        )

        if response.status_code != 200:
            raise Exception(
                "Скорей всего протух токен. " \
                "Нужно получить новый в браузере и сохранить его в файле " \
                "Data/request_data.txt. Либо проблема в dest, нужно указать свой dest " \
                "из браузера"
            )

        try:
            return response.json()
        except:
            raise Exception("невозможно преобразовать в json")