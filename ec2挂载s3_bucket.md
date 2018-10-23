官网：
https://github.com/s3fs-fuse/s3fs-fuse


# 0.IAM key,id
echo ACCESS_KEY_ID:SECRET_ACCESS_KEY > ~/.passwd-s3fs
chmod 600 /etc/passwd-s3fs

# 1./etc/fstab 自动挂载
/etc/fstab:
devops.zhangyh-test /data_s3/packages/ fuse.s3fs _netdev,allow_other 0 0
or
s3fs#devops.zhangyh-test /data_s3/packages/ fuse _netdev,allow_other,use_path_request_style,url=http://url.to.s3/,endpoint=cn-north-1 0 0

# 2.手动挂载
s3fs -o allow_other devops.zhangyh-test /data_s3/packages/ -o passwd_file=~/.passwd-s3fs -o url=http://s3.cn-north-1.amazonaws.com.cn -o endpoint=cn-north-1                                  //直接挂载,日志在/var/log/messages
s3fs -o allow_other devops.zhangyh-test /data_s3/packages/ -o passwd_file=~/.passwd-s3fs -o url=http://s3.cn-north-1.amazonaws.com.cn -o endpoint=cn-north-1 -o dbglevel=info -f -o curldbg   //带debug日志输出

# 3.查看
df -h
Filesystem                 Size  Used Avail Use% Mounted on
/dev/xvda1                 7.2G  3.8G  3.1G  56% /
devtmpfs                   3.6G     0  3.6G   0% /dev
tmpfs                      3.5G     0  3.5G   0% /dev/shm
tmpfs                      3.5G  338M  3.2G  10% /run
tmpfs                      3.5G     0  3.5G   0% /sys/fs/cgroup
/dev/xvdb1                 7.8G  134M  7.3G   2% /var/log
/dev/mapper/VG--SD-LV--SD  1.1T   66G  985G   7% /data
tmpfs                      707M     0  707M   0% /run/user/1002
s3fs                       256T     0  256T   0% /data_s3/packages

# 参考：
https://github.com/s3fs-fuse/s3fs-fuse/wiki/FAQ#q-https-connecting-failed-if-bucket-name-includes-dot-
https://aws.amazon.com/cn/blogs/china/s3fs-amazon-ec2-linux/
