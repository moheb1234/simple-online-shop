# Generated by Django 4.1.3 on 2022-12-08 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.SmallIntegerField(default=1),
        ),
    ]
