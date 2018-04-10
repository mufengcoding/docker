# 03 记一次docker下tomcat生成水印图片字体乱码


现象生成的图片上中文字体成了□□□□□这种类型

检查容器字体，发现中文字体是空的

##### 添加字体


首先把需要的字体放到共享的目录下

docker exec -it demo /bin/bash



1.字体拷贝,比如拷贝宋体

cp simsun.ttc /usr/share/fonts/


扫描生成字体

fc-cache -fv 

查看字体

fc-list :lang=zh 


docker restart demo
再次生成字体发现字体正常了