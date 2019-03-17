# docker


### 直接启动
```
docker run -d --restart="always"  -p 8080:8080 --name=solo mufeng5619/solo_auto:release-1.0
```

### 外部文件升级启动

```
docker run -d -v ${pwd}/classes:/root/blog/WEB-INF/classes --restart="always"  -p 8080:8080 --name=solo mufeng5619/solo_auto:release-1.0
```

将配置文件放到solo/classes下面



联系我：mufeng5619@gmail.com

个人站：blog.mufengs.com
