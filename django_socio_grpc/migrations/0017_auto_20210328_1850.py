# Generated by Django 2.2 on 2021-03-28 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_grpc_framework', '0016_grcperrorcode_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='sociogrpcerrors',
            name='custom',
            field=models.BooleanField(default=False, verbose_name='Customized Error'),
        ),
        migrations.AddField(
            model_name='sociogrpcerrors',
            name='reason',
            field=models.CharField(db_index=True, default='', max_length=250, verbose_name='Reason Error'),
        ),
    ]
