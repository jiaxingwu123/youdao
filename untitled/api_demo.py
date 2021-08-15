import requests
from appium import webdriver
import json
url = "https://petstore.swagger.io/v2/user/wujx"
header = {
    'accept': 'application/json'
}
data1 = {
  "id": 0,
  "username": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0
}
res= requests.get(url=url,header = header,data=data1)    #get 的参数是通过params来传递的
print(res.status_code)
# print(res.content)
print(res.text)


# url2 = "http://mail.rd.netease.com/"
# data ={
#     'account_name':'wujx021',
#     'id':'password'
# }
# res1 = requests.post(url=url2,data=data)
# print(res1.status_code)