# Generated by Django 2.2.7 on 2019-11-15 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items_service', '0018_auto_20191112_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='admin_stopped_auction',
            field=models.BooleanField(default=False),
        ),
    ]