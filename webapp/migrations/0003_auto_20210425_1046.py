# Generated by Django 2.0.3 on 2021-04-25 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20210425_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg_info',
            name='usr_id',
            field=models.IntegerField(default=87, primary_key=True, serialize=False, unique=True),
        ),
    ]
