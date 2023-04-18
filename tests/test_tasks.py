
import pytest

from tasks.task1 import func1
from tasks.task2 import func2
from tasks.task4 import func4


@pytest.mark.parametrize("input,expected", [
        ([{'visit1': ['Москва', 'Россия']}, {'visit2': ['Дели', 'Индия']}], [{'visit1': ['Москва', 'Россия']}]),
        ([{'visit5': ['Париж', 'Франция']}, {'visit6': ['Лиссабон', 'Португалия']}], []),
        ([{'visit8': ['Тула', 'Россия']}, {'visit9': ['Курск', 'Россия']}],
            [{'visit8': ['Тула', 'Россия']}, {'visit9': ['Курск', 'Россия']}])
])
def test_task1(input, expected):
    assert func1(input) == expected

@pytest.mark.parametrize("input,expected", [
        ({'user1': [213, 213, 213, 15, 213], 'user2': [54, 54, 119, 119, 119]}, [119, 213, 54, 15]),
        ({'user1': [213, 213, 213, 15, 213], 'user2': []}, [15, 213]),
        ({}, [])
])
def test_task2(input, expected):
    assert set(func2(input)) == set(expected)

@pytest.mark.parametrize("input,expected", [
        ({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, "yandex"),
        ({'facebook': 55, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, "vk"),
        ({}, None)
])
def test_task4(input, expected):
    assert func4(input) == expected

