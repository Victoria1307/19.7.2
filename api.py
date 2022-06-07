import requests
import json


class Boxberry:
    def __init__(self):
        self.base_url = "https://api.boxberry.ru/"

    def get_list_cities(self, token: str):
        """ Метод получения списка всех городов"""
        path = f'json.php?token={token}&method=ListCities'
        url = self.base_url+path
        print(f'url: {url}')
        res = requests.get(url)
        print(f'res = {res}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_moscow_points(self, token: str, city_code: str):
        path = f'json.php?token={token}&method=ListPoints&prepaid=1&CityCode={city_code}&CountryCode=643'
        url = self.base_url + path
        print(f'url: {url}')
        res = requests.get(url)
        print(f'res = {res}')
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result


