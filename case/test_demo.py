# coding = utf-8
# author: wenhowe
# datetime: 2022/1/4 09:29
# software: PyCharm

from api.api_keyword import ApiKeyword
from tools.read_config import ReadConfig
from tools.read_yaml import ReadYaml
import pytest


class TestLogin:

    def test_case_login(self):
        read_yaml = ReadYaml()
        data = read_yaml.read_yaml()
        # print(data)

        # 创建read_config对象
        readconfig = ReadConfig()
        url = readconfig.read_config()

        # 执行用例
        # 实例化请求方法的关键字对象
        api_kd = ApiKeyword()
        headers = data['headers']
        login_url = url + data['api_path']['login']

        params = data['params']
        res_post = api_kd.post(url=login_url, headers=headers, params=params)
        print(res_post.json())
        assert res_post.json()['msg'] == '成功'


