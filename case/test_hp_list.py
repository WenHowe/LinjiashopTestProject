# coding = utf-8
# author: wenhowe
# datetime: 2022/1/4 09:03
# software: PyCharm
from api.api_keyword import ApiKeyword
from tools.read_config import ReadConfig
from tools.read_yaml import ReadYaml
import pytest
import unittest


class TestHPList(unittest.TestCase):

    def test_hp_list(self):
        # 创建read_yaml对象
        read_yaml = ReadYaml()
        data = read_yaml.read_yaml()
        # print(data)

        # 创建read_config对象
        readconfig = ReadConfig()
        url = readconfig.read_config()

        # 实例化请求方法的关键字对象
        api_kd = ApiKeyword()
        headers = data['headers']
        list_url = url + data['api_path']['list']

        res_get = api_kd.get(url=list_url, headers=headers)
        print(res_get.json())
        assert res_get.json()['msg'] == '成功'
