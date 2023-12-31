# Generated by Django 4.1.3 on 2023-01-10 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_rename_current_bid_bid_old_bid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='new_bid',
            new_name='bid_amount',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='old_bid',
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.IntegerField(),
        ),
    ]
