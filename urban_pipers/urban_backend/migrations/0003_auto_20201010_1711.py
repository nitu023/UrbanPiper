# Generated by Django 3.1.2 on 2020-10-10 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urban_backend', '0002_category_is_delete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditems',
            name='is_veg',
        ),
        migrations.AddField(
            model_name='category',
            name='is_veg',
            field=models.BooleanField(default=False),
        ),
    ]
