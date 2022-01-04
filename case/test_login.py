# coding = utf-8
# author: wenhowe
# datetime: 2022/1/4 06:53
# software: PyCharm
import configparser

from api.api_keyword import ApiKeyword
from tools.read_config import ReadConfig
import pytest
import unittest
from ddt import ddt, file_data


@ddt
class TestLogin(unittest.TestCase):

    @file_data('../data/test_login.yaml')
    def test_case_login(self, **kwargs):
        readconfig = ReadConfig()
        url = readconfig.read_config()

        # 执行用例
        # 实例化请求方法的关键字对象
        api_kd = ApiKeyword()
        headers = kwargs['headers']
        login_url = url + kwargs['api_path']
        print(login_url)

        params = kwargs['params']
        res_post = api_kd.post(url=login_url, headers=headers, params=params)
        print(res_post.json())
        assert res_post.json()['msg'] == '成功'
