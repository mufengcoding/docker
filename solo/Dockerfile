FROM openjdk:8u181
MAINTAINER mufeng5619@gmail.com

WORKDIR /root
##下载安装包到root目录
# RUN wget https://github.com/b3log/solo/releases/download/v3.1.0/solo-v3.1.0.war
RUN wget https://github.com/b3log/solo/releases/download/v3.1.0/solo-v3.1.0.war
RUN wget -P /root https://raw.githubusercontent.com/mufengcoding/docker/master/solo/run.sh
RUN chmod u+x /root/run.sh

#ADD solo-v3.1.0.war /root/solo-v3.1.0.war
##解压并删除war包
#RUN unzip solo-v3.1.0.war -d /root/blog &&rm -rf solo-v3.1.0.war
RUN unzip solo-v3.1.0.war -d /root/blog &&rm -rf solo-v3.1.0.war
WORKDIR /root/blog

##启动博客
CMD ["/root/run.sh"]
