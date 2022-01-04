# coding = utf-8
# author: wenhowe
# datetime: 2022/1/4 06:44
# software: PyCharm
import requests


# 封装requests库请求关键字，避免频繁调用请求方法
class ApiKeyword(object):

    # 封装get方法
    def get(self, url, headers=None, params=None):
        return requests.get(url=url, headers=headers, params=params)

    # 封装post方法
    def post(self, url, headers=None, params=None):
        return requests.post(url=url, headers=headers, data=params)
