# Generated by Django 3.1.2 on 2020-11-07 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("volunteer", "0003_auto_20201107_2211"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="volunteerregistration",
            options={"verbose_name": "Volunteer Registration"},
        ),
        migrations.RenameField(
            model_name="volunteer",
            old_name="id",
            new_name="user",
        ),
        migrations.AlterField(
            model_name="volunteerregistration",
            name="was_present",
            field=models.BooleanField(
                default=False,
                verbose_name="Check if the volunteer was present on the event",
            ),
        ),
    ]
