# Generated by Django 2.2.6 on 2019-11-12 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items_service', '0017_items_has_bids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='item_pic',
            field=models.TextField(null=True),
        ),
    ]