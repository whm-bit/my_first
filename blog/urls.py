from django.urls import path,include # 引进路由配置相关包

import blog.views # 引入刚才实现的路由文件

urlpatterns = [  # 路由配置
    path('hello_world',blog.views.hello_world) # 如果url中含有hello_world，就把转到blog.views.hello_world视图函数里面
]