# Generated by Django 2.0.3 on 2018-03-15 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_airline_qqame'),
    ]

    operations = [
        migrations.AddField(
            model_name='airline',
            name='ssssame',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
