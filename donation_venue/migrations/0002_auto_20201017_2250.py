# Generated by Django 3.1.2 on 2020-10-17 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("donation_venue", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="donationvenue",
            options={"verbose_name": "Donation Venue"},
        ),
        migrations.AlterField(
            model_name="donationvenue",
            name="phone_number",
            field=models.BigIntegerField(verbose_name="Phone Number"),
        ),
    ]