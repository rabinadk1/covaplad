# Generated by Django 3.1.4 on 2020-12-16 11:44

from django.db import migrations, models

import donor.models


class Migration(migrations.Migration):

    dependencies = [
        ("donor", "0011_merge_20201216_1728"),
    ]

    operations = [
        migrations.AlterField(
            model_name="testreport",
            name="report",
            field=models.ImageField(
                unique=True, upload_to=donor.models.TestReport.donor_directory_path
            ),
        ),
    ]