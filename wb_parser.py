import requests

import Data.data_classes as data_classes

def get_token() -> str:
    try:
        with open("Data/request_data.txt") as file:
            return file.readline()
    except:
        raise Exception("" \
            "Невозможно получить токен из файла Data/request_data.txt. " \
            "Проверьте содержимое или наличие файла"
        )

def make_request_data(token: str, dest: int = -3115289) -> data_classes.RequestData:
    cookies = {
        'x_wbaas_token': token,
    }

    params = {
        'ab_testing': 'false',
        'appType': '1',
        'curr': 'rub',
        'dest': dest,
        'inheritFilters': 'false',
        'lang': 'ru',
        'query': 'пальто женское весна-осень',
        'resultset': 'catalog',
        'sort': 'popular',
        'spp': '30',
        'suppressSpellcheck': 'false',
    }

    return data_classes.RequestData(cookies=cookies, params=params)

def make_request(params: dict, cookies: dict):
    response = requests.get(
        'https://www.wildberries.ru/__internal/u-search/exactmatch/ru/common/v18/search',
        params=params,
        cookies=cookies
    )

    if response.status_code != 200:
        raise Exception("Скорей всего протух токен. " \
        "Нужно получить новый в браузере и сохранить его в файле " \
        "Data/request_data.txt. Либо проблема в dest, нужно указать свой dest " \
        "из браузера")

def main():
    request_data = make_request_data(token=get_token())
    make_request(
        params=request_data.params, 
        cookies=request_data.cookies
    )

if __name__ == "__main__":
    main()