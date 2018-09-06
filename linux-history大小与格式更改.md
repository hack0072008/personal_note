

# 前提：
    rpm -q bash
    bash-3.0以上版本有效

# 修改：vim /etc/bashrc
    HISTFILESIZE=2000
    HISTSIZE=2000
    HISTTIMEFORMAT="%Y%m%d-%H:%M:%S "  或者HISTTIMEFORMAT="%Y%m%d %T "
    export HISTTIMEFORMAT

# 生效：
    保存后退出，关闭当前shell，并重新登录
    (在~/.bash_history文件中，就有记录命令执行的时间)

# 注意：
    本方法必须在服务器刚刚新安装好时候，就设置这个参数。
    如果是已经运行了很久的服务器才添加这个参数，则以前的那些命令历史记录是不显示时间的。



~完~

