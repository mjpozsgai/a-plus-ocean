# Generated by Django 2.2.6 on 2019-11-14 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('cart_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('account_id', models.IntegerField()),
                ('item_id', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
