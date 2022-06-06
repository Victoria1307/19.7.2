from api import Boxberry
from settings import TOKEN

boxberry = Boxberry()


def test_get_list_cities(token=TOKEN):
    """ Проверяем получение списка городов, список не пустой и в каждом объекте города есть поле UniqName"""

    status, result = boxberry.get_list_cities(token)
    assert status == 200
    assert len(result) > 0
    assert 'UniqName' in result[0]