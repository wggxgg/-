from django.db import models

# Create your models here.

class CommodityInfos(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,verbose_name='商品名称')
    sezes=models.CharField(max_length=100,verbose_name='颜色')
    types=models.CharField(max_length=100,verbose_name='类型')
    price=models.FloatField(verbose_name='价格')
    discount=models.FloatField(verbose_name='折后')
    stock=models.IntegerField(verbose_name='库存')
    sold=models.IntegerField(verbose_name='已售')
    likes=models.IntegerField(verbose_name='收藏')
    created=models.DateField(auto_now_add=True,verbose_name='上架日期')
    img=models.FileField(upload_to=r'imgs/',verbose_name='商品图')
    detalis=models.FileField(upload_to=r'details',verbose_name='商品介绍')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='商品'
        verbose_name_plural='商品'

class Types(models.Model):
    id=models.AutoField(primary_key=True)
    firsts=models.CharField(max_length=100,verbose_name='一级分类')
    seconds=models.CharField(max_length=100,verbose_name='二级分类')
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name='商品类型'
        verbose_name_plural='类型'