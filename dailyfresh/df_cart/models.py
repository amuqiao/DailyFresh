from django.db import models
from df_goods.models import *
from df_user.models import *
# Create your models here.

class CartInfo(models.Model):
    goods = models.ForeignKey(GoodsInfo)
    count = models.IntegerField()
    user = models.ForeignKey(User_info)
    class Meta:
        db_table = 'Cart_info'



