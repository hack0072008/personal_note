#### 参考：
     https://www.jianshu.com/p/0e1e85808752

#### 安装:
     yum install aide
     aide -h
     
#### 配置：
    vim /etc/aide.conf
    #监控 /app 目录
    /app mon
    #排出 /app/f3 文件
    !/app/f3

#### 数据初始化：
     aide -i
     ls -ltrh  /var/lib/aide/aide.db.new.gz

#### 文件扫描：
     aide -C

#### 扫描结果更新到数据文件：
     aide -u
     cp -ar /var/lib/aide/aide.db.new.gz /var/lib/aide/aide.db.gz




----完----

