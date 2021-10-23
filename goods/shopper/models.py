from django.db import models

# Create your models here.
class CartInfos(models.Model):
    id=models.AutoField(primary_key=True)
    quantity=models.IntegerField(verbose_name='购买数量')
    commodity_id=models.IntegerField(verbose_name='商品id')
    user_id=models.IntegerField(verbose_name='用户id')
    class Meta:
        verbose_name_plural='购物车'

STATE=(
    ('待支付','待支付'),
    ('已支付','已支付'),
    ('发货中','发货中'),
    ('已签收','已签收'),
    ('退货中','退货中'),
)

class OrderInfos(models.Model):
    id=models.AutoField(primary_key=True)
    price=models.FloatField(verbose_name='订单总价')
    created=models.DateField(auto_now_add=True,verbose_name='创建时间')
    user_id=models.IntegerField(verbose_name='用户id')
    state=models.CharField(max_length=50,choices=STATE,verbose_name='订单状态')
    class Meta:
        verbose_name_plural='订单'