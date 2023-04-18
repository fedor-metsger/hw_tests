
import json
import random

import requests
from datetime import datetime

BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"
FILES_URL = "https://cloud-api.yandex.net/v1/disk/resources/files"
UPLOAD_URL = "https://cloud-api.yandex.net/v1/disk/resources/upload"

YA_TOKEN_FILE = "ya_token.txt"

def load_ya_token(fname):
    """
    Загружает токен для работы с Yandex из файла
    """
    l = None
    try:
        with open(YA_TOKEN_FILE) as inf:
            l = inf.readline()
            if not l or l == '':
                raise ValueError("Файл не содержит токен")
    except Exception as e:
        print(f'Ошибка при чтении файла {YA_TOKEN_FILE}: ', str(e))
        print(f'Должены быть создан файл {YA_TOKEN_FILE},\n"'
              f'в первой строке содержащий токен для доступа к яндекс диску')
    return l


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": "OAuth {}".format(self.token)
        }

    def get_files_list(self):
        """
        Метод возвращает список файлов на яндекс диске
        """
        headers = self.get_headers()
        params = {"limit": 1000}
        response = requests.get(FILES_URL, headers=headers, params=params)
        #        print(response.json())
        return response.json()

    def check_exist(self, path):
        """
        Метод Проверяет наличие файла или каталога
        """
        headers = self.get_headers()
        params = {"path": path}
        response = requests.get(BASE_URL, headers=headers, params=params)
        return response.status_code == 200

    def mkfolder(self, dir_name):
        """
        Метод создаёт папку (каталог) на яндекс диске
        """
        params = {"path": dir_name}
        response = requests.put(BASE_URL, headers=self.get_headers(), params=params)

        return response

def main():

    ya_token = load_ya_token(YA_TOKEN_FILE)


    uploader = YaUploader(ya_token)
    dir_name = "test_" + str(random.randint(0, 9999)).zfill(4)
    print(f"Создаю папку {dir_name}")
    print(f'Возврат: {uploader.mkfolder(dir_name)}')
    files = uploader.get_files_list()
    [print(n["name"], n["type"]) for n in files["items"]]
    print(f"Снова создаю папку {dir_name}")
    print(f'Возврат: {uploader.mkfolder(dir_name)}')

    uploader.check_exist("test_20230418135529")
    uploader.check_exist("test_202")

if __name__ == "__main__":
    main()