
# 坑一：
    flask返回data时 render_template的 json对象数据，在jinjia2模板js中 {{ data }} 自动转换成str,而且是assic编码
    解决办法：{{ data|tojson }}
    参考：https://blog.csdn.net/baidu_36831253/article/details/79067838
    





~待续~

