# Generated by Django 2.2.7 on 2019-11-17 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_service', '0002_remove_accounts_address_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watchlists',
            fields=[
                ('watchlist_id', models.AutoField(primary_key=True, serialize=False)),
                ('desired_item', models.CharField(max_length=100)),
                ('desired_price', models.FloatField(null=True)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts_service.Accounts')),
            ],
        ),
    ]