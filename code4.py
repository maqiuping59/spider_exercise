from selenium import webdriver
import urllib.request
import pprint
# urllib 构造请求方法1，urlopen()方法
response = urllib.request.urlopen('https://www.baidu.com/')
print(type(response))
print(response.status)
print(response.reason)
print(response.debuglevel)
print(response.read)
headers = {}
for i,j in response.getheaders():
    headers[i]=j

pprint.pprint(headers)
try:
    print(headers['Set-Cookie'])

except KeyError as e:
    print(e)