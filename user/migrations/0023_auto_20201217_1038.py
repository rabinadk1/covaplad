# Generated by Django 3.1.4 on 2020-12-17 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0022_auto_20201216_2333"),
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