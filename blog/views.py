from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# 在这里面写视图函数

def hello_world(request): # request参数是http请求的对象
    return HttpResponse("Hello,World")

"""

Django路由
runserver可以看到Django欢迎页面
请求没办法到达刚才的视图函数
需要配置路由绑定视图函数和URL

    先配置应用层次的路由：在blog目录下新建一个文件urls.py
    然后完成项目层次的路由配置：到django_introduction中打开urls.py
    最后把blog应用添加到配置文件里面，就是django_introduction中的settings.py    
"""