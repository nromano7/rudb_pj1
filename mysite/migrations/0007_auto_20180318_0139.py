# Generated by Django 2.0.3 on 2018-03-18 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_auto_20180318_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='dst_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='route',
            name='src_time',
            field=models.TimeField(),
        ),
    ]
