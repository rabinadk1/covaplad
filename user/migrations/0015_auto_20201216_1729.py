# Generated by Django 3.1.4 on 2020-12-16 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0014_merge_20201216_1728"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="user",
            name="user_gender_in_valid_choices",
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.CheckConstraint(
                check=models.Q(gender__in=("M", "F", "L", "G", "B", "T", "N")),
                name="user_gender_in_valid_choices",
            ),
        ),
    ]