# Generated by Django 2.2 on 2021-03-28 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_grpc_framework', '0015_auto_20210328_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='grcperrorcode',
            name='reason',
            field=models.CharField(db_index=True, default='', max_length=250, verbose_name='Reason Error'),
        ),
    ]
