# Generated by Django 2.2.6 on 2019-11-11 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items_service', '0012_auto_20191111_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='category_id',
        ),
    ]
