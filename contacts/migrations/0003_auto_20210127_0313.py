# Generated by Django 3.1.5 on 2021-01-27 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20210127_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='car_id',
            field=models.IntegerField(),
        ),
    ]
