# Celery

## install
    pip install celery
    pip install django-celery
## monitor
    pip install flower

## words
    先了解了几个常用的参数的含义：
    Exchange:交换机，决定了消息路由规则；
    Queue:消息队列；
    Channel:进行消息读写的通道；
    Bind:绑定了Queue和Exchange，意即为符合什么样路由规则的消息，将会放置入哪一个消息队列；

## 启动参数
    参考：http://docs.celeryproject.org/en/latest/reference/celery.bin.worker.html#cmdoption-celery-worker-c
    
    -c, --concurrency
    Number of child processes processing the queue. The default is the number of CPUs available on your system.

    -P, --pool
    Pool implementation:
    prefork (default), eventlet, gevent or solo.

    -n, --hostname
    Set custom hostname (e.g., 'w1@%%h‘). Expands: %%h (hostname), %%n (name) and %%d, (domain).

    -Q, --queues
    List of queues to enable for this worker, separated by comma. By default all configured queues are enabled. Example: -Q video,image

    -f, --logfile
    Path to log file. If no logfile is specified, stderr is used.

    -l, --loglevel
    Logging level, choose between DEBUG, INFO, WARNING, ERROR, CRITICAL, or FATAL.

    --purge
    Purges all waiting tasks before the daemon is started. WARNING: This is unrecoverable, and the tasks will be deleted from the messaging server.

    --autoscale
    Enable autoscaling by providing max_concurrency, min_concurrency. Example:
    --autoscale=10,3

    --prefetch-multiplier
    Set custom prefetch multiplier value for this worker instance.
    
## 启动
    python manage.py celery worker -f /var/log/celery_work_others.log --autoscale=4,2 -l INFO -n worker_others -Q default,consul_queue,package_queue,pre_process_queue,deregister_queue,register_queue
    celery flower --broker=redis://:redis_password@127.0.0.1:6379/1 --address=0.0.0.0 --port=5555 --basic_auth=username:password
## 清除celery队列待执行任务
    celery purge -Q queuename    #清除指定队列任务
    celery purge                 #清除所有任务

## 配置
    默认路由规则：http://docs.jinkan.org/docs/celery/userguide/routing.html#id2
    队列配置：http://docs.jinkan.org/docs/celery/userguide/routing.html#how-the-queues-are-defined
    配置项：http://docs.celeryproject.org/en/master/userguide/configuration.html#new-lowercase-settings

## 优化参数
    https://www.v2ex.com/t/343440
    http://docs.celeryproject.org/en/master/userguide/optimizing.html#optimizing-prefetch-limit

## 代码结构
    .
    ├── manage.py
    ├── platform3
    │   ├── admin.py
    │   ├── apps.py
    │   ├── common
    │   │   └── __init__.py
    │   ├── __init__.py
    │   ├── __init__.pyc
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── service
    │   ├── tasks.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    └── Sengladmin
       ├── __init__.py
       ├── __init__.pyc
       ├── settings.py
       ├── static
       │   ├── css
       │   ├── fonts
       │   ├── image
       ├── templates
       ├── urls.py
       └── wsgi.py

## setting.py
    import djcelery
    djcelery.setup_loader()
    from kombu import Queue,Exchange

    CELERY_DEFAULT_QUEUE = 'default'
    CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
    CELERY_DEFAULT_ROUTING_KEY = 'default'

    CELERY_RESULT_SERIALIZER = 'json'

    BROKER_URL = 'redis://:seng1admin@127.0.0.1:6379/1'
    CELERY_RESULT_BACKEND = 'redis://:seng1admin@127.0.0.1:6379/1'
    #CELERY_TASK_RESULT_EXPIRES = 86400
    CELERY_IMPORTS = ('platform3.tasks',)

    #CELERYD_PREFETCH_MULTIPLIER = 4
    CELERY_QUEUES = (
        Queue(name='default',       exchange=Exchange('default', type='direct'),       routing_key='default'),
        Queue(name='consul_queue',  exchange=Exchange('consul', type='direct'),  routing_key='consul.#'),
    )
    
    CELERY_ROUTES = ({
        'consul_sync_datacenter': {'queue': 'consul_queue', 'routing_key': 'consul.consul_sync_datacenter'},
    })



## tasks.py
    from celery import task,platforms
    from celery.utils.log import get_task_logger
    platforms.C_FORCE_ROOT = True

    from django.conf import settings
    import os
    import time
    
    logger = get_task_logger(__name__)

    @task()
    def consul_add_group(*args, **kwargs):
      time.sleep(30)
      logger.info('consul_add_group...')
      return True

## views.py
    ...
    def test_tasks(request):
    if request.method == 'GET':
        consul_add_group.apply_async(queue = 'consul_queue')
        return HttpResponse('ok')
    ...
## test by shell
    python manage.py shell
    from platform3.tasks import *
    consul_add_group.apply_async(queue = 'consul_queue')
    
## log
    tail -f /var/log/celery_work_others.log






















