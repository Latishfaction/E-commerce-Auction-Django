# Generated by Django 4.1.7 on 2023-06-24 18:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0029_orderhistory"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orderhistory",
            old_name="product",
            new_name="product_info",
        ),
    ]
