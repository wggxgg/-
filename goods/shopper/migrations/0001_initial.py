# Generated by Django 3.2.7 on 2021-10-11 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(verbose_name='购买数量')),
                ('commodity_id', models.IntegerField(verbose_name='商品id')),
                ('user_id', models.IntegerField(verbose_name='用户id')),
            ],
            options={
                'verbose_name_plural': '购物车',
            },
        ),
        migrations.CreateModel(
            name='OrderInfos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.FloatField(verbose_name='订单总价')),
                ('created', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('user_id', models.IntegerField(verbose_name='用户id')),
                ('state', models.CharField(choices=[('待支付', '待支付'), ('已支付', '已支付'), ('发货中', '发货中'), ('已签收', '已签收'), ('退货中', '退货中')], max_length=50, verbose_name='订单状态')),
            ],
            options={
                'verbose_name_plural': '订单',
            },
        ),
    ]
