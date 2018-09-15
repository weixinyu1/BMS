# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# 书籍类型
class BookType(models.Model):
    # 书籍类型名称
    tname=models.CharField(max_length=20,unique=True,verbose_name='类型')


# 书籍信息
class Book(models.Model):
    # 书籍编号
    bid=models.PositiveIntegerField(primary_key=True,unique=True,verbose_name='书籍编号')
    # 书籍名称
    bname=models.CharField(max_length=30,verbose_name='图书名称')
    # 书籍类型
    btype=models.ForeignKey(BookType,on_delete=models.CASCADE,verbose_name='书籍类型')



# 管理员
class admin(models.Model):
    # 管理员编号
    aid=models.AutoField(primary_key=True,verbose_name='编号')
    # 管理员名称
    aname=models.CharField(max_length=30,verbose_name='管理员名称')



# 用户
class User(models.Model):
    # 用户id
    uid=models.AutoField(primary_key=True,verbose_name='编号')
    # 用户名称
    uname=models.CharField(max_length=30,verbose_name='用户')
    # 用户密码
    upwd=models.CharField(max_length=20,verbose_name='密码')
    # 注册时间
    created=models.DateField(auto_now_add=True,verbose_name='注册时间')



# 用户借书表
class Userborrow(models.Model):
    # 借书用户名
    unmae=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户id')
    # 所借书籍
    bname=models.ForeignKey(Book,verbose_name='书籍名称')
    # 借书时间
    created=models.DateTimeField(auto_now_add=True,verbose_name='借书时间')