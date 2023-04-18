
import random
import pytest
from yandex import YaUploader, load_ya_token, YA_TOKEN_FILE

@pytest.fixture
def dir_name():
    return "test_" + str(random.randint(0, 99999)).zfill(5)

def test_yandex1(dir_name):
    ya = YaUploader('qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq')
    result = ya.mkfolder(dir_name)
    assert result.status_code == 401

def test_yandex2(dir_name):
    ya = YaUploader(load_ya_token(YA_TOKEN_FILE))
    result = ya.mkfolder(dir_name)
    assert result.status_code == 201

def test_yandex3(dir_name):
    ya = YaUploader(load_ya_token(YA_TOKEN_FILE))
    result = ya.mkfolder(dir_name)
    assert result.status_code == 201
    result = ya.mkfolder(dir_name)
    assert result.status_code == 409

def test_yandex4(dir_name):
    ya = YaUploader(load_ya_token(YA_TOKEN_FILE))
    result = ya.mkfolder(dir_name)
    assert ya.check_exist(dir_name)

