# Generated by Django 4.1.6 on 2023-02-12 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("count_day", "0005_alter_count_day_time"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="count_day",
            name="time",
        ),
    ]
