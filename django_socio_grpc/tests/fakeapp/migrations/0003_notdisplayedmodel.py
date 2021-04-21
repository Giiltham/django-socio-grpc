# Generated by Django 3.2 on 2021-04-21 16:33

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fakeapp", "0002_foreignmodel_manymanymodel_relatedfieldmodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="NotDisplayedModel",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
    ]
