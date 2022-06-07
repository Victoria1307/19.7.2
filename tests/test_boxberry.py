from api import Boxberry
from settings import TOKEN

boxberry = Boxberry()


def test_get_list_cities(token=TOKEN):
    """ Проверяем получение списка городов, список не пустой и в каждом объекте города есть поле UniqName"""

    status, result = boxberry.get_list_cities(token)
    assert status == 200
    assert len(result) > 0
    assert 'UniqName' in result[0]


def test_get_moscow_points(token=TOKEN):
    """Проверяем получение все точек в Москве"""
    status, result = boxberry.get_moscow_points(token, '68', '643')
    assert status == 200
    assert len(result) > 0
    assert 'Metro' in result[0]


def test_get_city_points_not_found(token=TOKEN):
    """Проверяем получение все точек с несуществующем кодом города """
    status, result = boxberry.get_moscow_points(token, '10001', '643')
    assert status == 200
    assert len(result) == 1
    assert result[0].get('err') == 'Данные не найдены'


def test_get_city_points_not_found(token=TOKEN):
    """Проверяем получение все точек с несуществующем кодом страны """
    status, result = boxberry.get_moscow_points(token, '68', '77777')
    assert status == 200
    assert len(result) == 1
    assert result[0].get('err') == 'Данные не найдены'


def test_get_zips(token=TOKEN):
    """Проверяем получения списка ZIP кодов"""
    status, result = boxberry.get_list_zips(token)
    assert status == 200
    assert len(result) > 1
    assert 'Zip' in result[0]
    assert 'City' in result[0]


def test_check_zip(token=TOKEN):
    """Проверяем метод проверки данных по определенному ZIP коду"""
    status, result = boxberry.check_zip(token, '108818')
    assert status == 200
    assert len(result) == 1
    assert 'ExpressDelivery' in result[0]


def test_check_unknown_zip(token=TOKEN):
    """Проверяем метод проверки данных по определенному ZIP коду"""
    status, result = boxberry.check_zip(token, '12')
    assert status == 200
    assert len(result) == 1
    assert result.get('err') == 'Данные не найдены'
