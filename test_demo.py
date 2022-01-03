# coding = utf-8
# author: wenhowe
# datetime: 2022/1/4 05:18
# software: PyCharm
import requests
headers = {"content-type": "application/json;charset=UTF-8"}
response = requests.get(url="http://api.tech-developer.tk:8080/dev-api/category/list", headers=headers)
result = response.json()
print(result)

if (result["code"] == 20000) :
    print('-' * 50 )
    print("请求正确")
    print('-' * 50 )

