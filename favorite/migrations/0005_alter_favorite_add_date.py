# Generated by Django 4.1.3 on 2022-12-09 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorite', '0004_alter_favorite_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
