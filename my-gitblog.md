

#### 软硬件配置：
    树莓派3B+
    官方：2018-11-13-raspbian-stretch.zip（1.0G）
    
#### 软件安装
    apt-get install php
    Failed to start The Apache HTTP Server.()与nginx默认端口冲突)
    apt-get install php-mysql
    apt-get install php-fpm
    apt-get install php-mbstring
#### 软件配置
    vim /etc/apache2/ports.conf
    Listen 8080
    Listen 1443
    /etc/init.d/apache2 restart

#### 安装部署
    root@pi:/var/www# ll
    total 12
    drwxr-xr-x 2 root root 4096 Nov 30 12:26 html
    -rw-r--r-- 1 root root   19 Nov 30 13:47 index.php
    drwxr-xr-x 3 root root 4096 Nov 30 13:51 blog
    root@pi:/var/www# cat index.php 
    <?php phpinfo();?>

#### 502错误
    cd /var/www/blog/gitblog-2.3.2
    chown -R root:root ./app/cache
    chown -R root:root ./app/logs
#### 其他配置
    vim /etc/php/7.0/apache2/php.ini
    short_open_tag = On

#### 重启服务
    /etc/init.d/apache2 restart
    /etc/init.d/nginx restart



