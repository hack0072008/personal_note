

### 参考：
    http://www.cnblogs.com/goozgk/p/5658137.html

### 安装：
    yum install lvm2



### 新增详细步骤：
    add disk
    fdisk /dev/xvdg      //lvm:t,L,8e
    partprobe
    pvcreate /dev/xvdg1
    pvs
    vgcreate docker_data01 /dev/xvdg1
    vgs
    lvcreate -L 99.99g -n lv01 docker_data01
    lvs
    mkfs.ext4 /dev/docker_data01/lv01
    mkdir -p /mnt/data2
    mount /dev/docker_data01/lv01 /mnt/data1/








~~完~~


