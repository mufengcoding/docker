#!/bin/bash
source /etc/profile
cd /root/blog 
java -cp WEB-INF/lib/*:WEB-INF/classes org.b3log.solo.Starter
