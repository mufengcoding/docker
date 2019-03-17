# _*_ coding:utf-8 _*_
import  requests, json


# 指定api地址
api_url = 'https://api.github.com/repos/b3log/solo/releases/latest'



r = requests.get(api_url)


a = json.dumps(r.json())
b = json.loads(a)
# print a
print b['name']