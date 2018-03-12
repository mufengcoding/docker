FROM node:6
MAINTAINER Mufeng <mufeng5619@gmail.com>

RUN npm i docsify-cli -g

RUN mkdir docs
RUN docsify init ./docs
 

EXPOSE 3000
CMD docsify serve docs