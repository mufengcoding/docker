# _*_ coding:utf-8 _*_
import  requests, json,os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 指定api地址
api_url = 'https://api.github.com/repos/b3log/solo/releases/latest'
r = requests.get(api_url)
a = json.dumps(r.json())
b = json.loads(a)
# print a
print b['name']
f = open('/root/docker/solo/Dockerfile', 'r')
content = f.read()
f.close()

t = content.replace("3.2.0",b['name'])
t = content.replace("3.3.0","3.1.0")
with open("/root/docker/solo/Dockerfile","w") as f2:
    f2.write(t)
#os.system('git tag -a '+b["name"])
os.system('git tag -a 3.1.0')
os.system('git commit -a -m 123')
os.system('git push')
