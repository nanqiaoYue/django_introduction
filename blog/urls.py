# 管理路由
from django.urls import path, include

import blog.views

urlpatterns = [
    path('hello', blog.views.hello),
]
