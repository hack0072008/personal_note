

#### import
    >>> import jenkins

#### connect
    >>> jk = jenkins.Jenkins(url = 'http://platform.xxxx.xxxx.com:9090', username='root', password='********', timeout = 60)

#### get jenkins version
    >>> version = jk.get_version()

#### get job config.xml
>>> admin_config = jk.get_job_config('admin-server')

#### modify job config.xml
...

#### modify job from config.xml
>>> ret = jk.reconfig_job('admin-server', admin_config)

#### create job from config.xml
>>> admin_2 = jk.create_job('admin-server-copy', admin_config)

#delete job
>>> ret = jk.delete_job('admin-server-copy')

#check job is exist
>>> ret = jk.job_exists('admin-server-copy')
>>> print ret
None
>>> ret = jk.job_exists('admin-server')
>>> ret
True

#get next build number
>>> next_build_number = jk.get_job_info('admin-server')['nextBuildNumber']

#build job
>>> output = server.build_job('admin-server')

#get job build info
>>> from time import sleep; sleep(10)
>>> build_info = jk.get_build_info('admin-server', next_build_number)
>>> print(build_info)

#get job build console info
>>> build_info = jk.get_build_console_output('admin-server', 105)



