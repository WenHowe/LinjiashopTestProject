# coding = utf-8
# author: wenhowe
# datetime: 2022/1/4 05:18
# software: PyCharm
import requests

headers = {"Accept": "application/json, text/plain, */*"}
url_get = "http://api.tech-developer.tk:8080/dev-api/category/list"
response_get = requests.get(url=url_get, headers=headers)
result_get = response_get.json()
# print(result_get)
# assert result_get["code"] == 20000

# if (result_get["code"] == 20000) :
#     print('-' * 50 )
#     print("首页请求正确")
#     print('-' * 50 )

print('')

url_post = "http://api.tech-developer.tk:8080/dev-api/loginByPass"
param_post = (("mobile", "10086"), ("password", "123456"))
# response_post = requests.post(url=url_post, data=param_post, headers=headers)
response_post = requests.post(url=url_post, data={'mobile': '10086', 'password': '123456'}, headers=headers)
result_post = response_post.json()
print(result_post)
assert result_post["code"] == 20000, '登陆失败'
if result_post["code"] == 20000:
    print('-' * 50)
    print("登陆成功")
    print('-' * 50)
