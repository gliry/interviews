# Generated by Django 2.2.10 on 2021-05-05 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0005_auto_20210505_1507"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answer", name="user_id", field=models.PositiveIntegerField(),
        ),
    ]
