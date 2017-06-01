# coding=utf-8
from django.db import models

# Create your models here.
# 定义user模型类
class User_info(models.Model):
    #用户信息
    user_name = models.CharField(max_length=20)
    user_passwd = models.CharField(max_length=40)
    user_mail = models.CharField(max_length=30)
    #用户中心
    consignee_name = models.CharField(max_length=20, default='')
    consignee_address = models.CharField(max_length=20, default='')
    consignee_postcode = models.CharField(max_length=20, default='')
    consignee_tel = models.CharField(max_length=20, default='')

    class Meta:
        db_table = 'user_info'