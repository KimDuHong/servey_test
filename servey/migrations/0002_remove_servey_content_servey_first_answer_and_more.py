# Generated by Django 4.1.6 on 2023-02-07 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("servey", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="servey",
            name="content",
        ),
        migrations.AddField(
            model_name="servey",
            name="first_answer",
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="servey",
            name="second_answer",
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
