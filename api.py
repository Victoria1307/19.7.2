import requests
import json


class Boxberry:
    def __init__(self):
        self.base_url = "https://api.boxberry.ru/"

    def get_list_cities(self, token: str):
        """ Метод получения списка всех городов"""
        path = f'json.php?token={token}&method=ListCities'
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

    def get_points(self, token: str, city_code: str, country_code: str):
        """Метод получения точек по коду города и страны"""
        path = f'json.php?token={token}&method=ListPoints&prepaid=1&CityCode={city_code}&CountryCode={country_code}'
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

    def get_point_description(self, token: str, point_code: str):
        """Получить полную информацию по пункту выдачи"""
        path = f'json.php?token={token}&method=PointsDescription&code={point_code}'
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

    def get_list_zips(self, token: str):
        """ Метод получения списка ZIP кодов"""
        path = f'json.php?token={token}&method=ListZips'
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

    def check_zip(self, token: str, zip_code: str):
        """Метод проверки ZIP кода"""
        path = f'json.php?token={token}&method=ZipCheck&Zip={zip_code}'
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

    def get_courier_list_cities(self, token: str):
        """ Получить перечень городов, в которых осуществляется курьерская доставка"""
        path = f'json.php?token={token}&method=CourierListCities'
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

    def get_point_for_parcels(self, token: str):
        """ Получить список пунктов приема посылок."""
        path = f'json.php?token=d6f33e419c16131e5325cbd84d5d6000&method=PointsForParcels'
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
