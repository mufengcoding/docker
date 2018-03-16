# 02 搭建vm的harbor仓库


#### 更新操作系统

> yum update

#### 安装基本环境

> yum install  -y docker && yum install docker-compose

> service docker start && systemctl enable docker

配置阿里云加速器
```
sudo tee /etc/docker/daemon.json <<-'EOF'
{
 "registry-mirrors": ["https://d8b3zdiw.mirror.aliyuncs.com"]
}
EOF
```

!> 这里可能因为软件源等因素docker-compose没安装成功,使用下面的方法 

?> sudo curl -L https://github.com/docker/compose/releases/download/1.19.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
 chmod +x /usr/local/bin/docker-compose 

```shell
[root@localhost ~]# docker-compose -v
docker-compose version 1.19.0, build 9e633ef

```
看到上述输出，则代表docker-compose安装成功

#### 初始化harbor

下载harbor并解压

?>wget https://storage.googleapis.com/harbor-releases/release-1.4.0/harbor-online-installer-v1.4.0.tgz  
tar -zxvf harbor-online-installer-v1.4.0.tgz  

进入harbor并初始化

?>cd harbor && ./install.sh

!>替换配置文件相关

sed -i 's#reg.mydomain.com#xxx#g' harbor.cfg  //修改访问地址

sed -i 's#8888#8888:80#g' docker-compose.yml  //修改nginx端口避免端口冲突


?>reating registry ... 
Creating harbor-adminserver ... 
Creating harbor-ui ... 
Creating nginx ... 
Creating harbor-jobservice ... 

?> ----Harbor has been installed and started successfully.----

?>Now you should be able to visit the admin portal at http://160.255.0.158. 
For more details, please visit https://github.com/vmware/harbor .

到这里就安装完成了

#### 使用

访问ip：8888可以出现harbor的界面
默认用户名密码
admin/Harbor12345