# Generated by Django 2.2.7 on 2019-11-17 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_service', '0003_watchlists'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='exdate',
            field=models.CharField(default='01/2020', max_length=7),
            preserve_default=False,
        ),
    ]
