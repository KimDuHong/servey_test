# Generated by Django 4.1.6 on 2023-02-07 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("result", "0002_alter_tendencies_options_result_count_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="kind",
            name="tendency",
            field=models.ManyToManyField(
                related_name="tendency", to="result.tendencies"
            ),
        ),
    ]
