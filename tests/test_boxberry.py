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
    status, result = boxberry.get_moscow_points(token, '68')
    assert status == 200
    assert len(result) > 0
    assert 'Metro' in result[0]

def test_get_city_points_not_found(token=TOKEN):
    """Проверяем получение все точек с несуществующем кодом города """
    status, result = boxberry.get_moscow_points(token, '10001')
    assert status == 200
    assert len(result) == 1
    assert result[0].get('err') == 'Данные не найдены'
