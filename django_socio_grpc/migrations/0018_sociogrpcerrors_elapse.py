# Generated by Django 2.2 on 2021-03-28 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_grpc_framework', '0017_auto_20210328_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='sociogrpcerrors',
            name='elapse',
            field=models.FloatField(default=0.0),
        ),
    ]
