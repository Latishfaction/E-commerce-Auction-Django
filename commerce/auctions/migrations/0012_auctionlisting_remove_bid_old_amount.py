# Generated by Django 4.1.3 on 2023-01-10 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_remove_bid_bidder_bid_bidder'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuctionListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='bid',
            name='old_amount',
        ),
    ]
