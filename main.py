
from tasks.task1 import func1
from tasks.task2 import func2
from tasks.task4 import func4

def main():

    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]
    print(func1(geo_logs))

    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
    print(func2(ids))

    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    print(func4(stats))

    

if __name__ == '__main__':
    main()
