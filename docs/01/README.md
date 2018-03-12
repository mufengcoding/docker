# 01 制作docsify镜像


### dockerfile如下

```shell
From Node:6
Maintainer Mufeng <Mufeng5619@Gmail.Com>
Run Npm I Docsify-Cli -G
Run Mkdir Docs
Run Docsify Init ./Docs
Expose 3000
Cmd Docsify Serve Docs
```


!> Maintainer 主要是作者信息

!> Cmd 后面直接跟命令 启动镜像的时候就不需要了 不然会覆盖

### 使用
```shell
docker build -t dockerdocs:1.2 .
docker run -d -p 8234:3000 --name="doc" -v /docs:/docs dockerdocs:1.2
```
这里需要注意一下的是  第一个宿主机的路径最好是全路径 不然有点小问题