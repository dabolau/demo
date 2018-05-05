from django.db import models
from datetime import *


# 用户登录数据库模型
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


# 商品数据库模型
class Product(models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    create_time = models.DateTimeField(default=datetime.now())
    update_time = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name
