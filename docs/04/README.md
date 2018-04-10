# 04 docker部署tomcat+nginx+mysql应用

##### 部署mysql

添加私有镜像加速器

将下面添加到/etc/docker/daemon.json里面

```shell
 "registry-mirrors": [
        "http://05924529.m.daocloud.io"
    ]
```   

重启docker
```shell
docker run —name db -p 3246:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:latest
```
查看mysql字符集

```mysql
use mysql;
show variables like '%char%';  
```

进入容器查看相应信息
```docker
docker exec -it db /bin/bash
```
需要暴露的目录

/var/log/mysql/

/etc/mysql/conf.d


将下面的配置添加到 /etc/mysql/conf.d/docker.conf下面
```
[mysqld]

character-set-server=utf8
collation-server=utf8_general_ci
sql_mode ='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION'
```


修改导入数据库sql大小限制

首先查看了下.sql文件大小为360M，然后使用sql语句查询数据库最大支持的大小：

SHOW GLOBAL VARIABLES LIKE 'max_allowed_packet';

随后根据需求对该值进行修改：

SET GLOBAL max_allowed_packet=1024*1024*400;


web
```
docker pull mufeng5619/tomcat

 docker run --name db -v $PWD/conf.d:/etc/mysql/conf.d -v $PWD/log:/var/log/mysql  -p 3446:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:latest
 ```

```
docker run --link db:db --name jsz -v $PWD/web_jsz/tomcat:/usr/local/tomcat  -p 8081:8080 -d --restart="always" docker.io/mufeng5619/tomcat:1.8
```


配置文件里面数据连接池那边直接写db:3246就可以