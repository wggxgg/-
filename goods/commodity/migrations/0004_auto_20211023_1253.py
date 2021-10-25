# Generated by Django 2.2 on 2021-10-23 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0003_alter_commodityinfos_details'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commodityinfos',
            options={'verbose_name': '商品', 'verbose_name_plural': '商品'},
        ),
        migrations.AlterModelOptions(
            name='types',
            options={'verbose_name': '商品类型', 'verbose_name_plural': '类型'},
        ),
        migrations.RemoveField(
            model_name='commodityinfos',
            name='details',
        ),
        migrations.AddField(
            model_name='commodityinfos',
            name='detalis',
            field=models.FileField(default='', upload_to='details', verbose_name='商品介绍'),
            preserve_default=False,
        ),
    ]
