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

print b['name']
f = open('/root/docker/solo/Dockerfile', 'r')
content = f.read()
f.close()
v = open('/root/docker/autoupdate/version', 'r')
vcontent = v.read()
v.close()
#t = content.replace(vcontent,b['name'])
t = content.replace("3.3.0","3.1.0")
with open("/root/docker/solo/Dockerfile","w") as f2:
    f2.write(t)
with open("/root/docker/autoupdate/version","w") as f1:
    f1.write(b['name'])
# os.system('git tag -a '+b["name"])
os.system('git tag -a 3.1.0 -m'+b['name'])
os.system('git commit -a -m '+b['name'])
os.system('git push')
os.system('git push origin --tags')
