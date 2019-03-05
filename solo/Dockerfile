FROM openjdk:8u181
MAINTAINER mufeng5619@gmail.com

##下载安装包到root目录
RUN wget https://github.com/b3log/solo/releases/download/v3.2.0/solo-v3.2.0.war
#ADD run.sh /root/run.sh
#ADD solo-v3.2.0.war /root/solo-v3.2.0.war
##解压并删除war包
RUN unzip solo-v3.2.0.war -d /root/blog &&rm -rf solo-v3.2.0.war
##启动博客
CMD java -cp WEB-INF/lib/*:WEB-INF/classes org.b3log.solo.Starter
