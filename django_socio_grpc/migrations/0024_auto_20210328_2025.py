# Generated by Django 2.2 on 2021-03-28 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_grpc_framework', '0023_auto_20210328_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grcpdatabases',
            name='django',
            field=models.CharField(choices=[('django.contrib.admin', 'Administration'), ('django.contrib.auth', 'Authentication and Authorization'), ('django.contrib.contenttypes', 'Content Types'), ('django.contrib.sessions', 'Sessions'), ('django.contrib.messages', 'Messages'), ('django.contrib.staticfiles', 'Static Files'), ('django_grpc_framework', 'Django_Grpc_Framework'), ('fcm_django', 'FCM Django'), ('carcheck', 'Carcheck'), ('notification', 'Notification'), ('user', 'User')], db_index=True, default='', max_length=40, verbose_name='Django Application'),
        ),
    ]
