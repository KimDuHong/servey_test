# Generated by Django 4.1.6 on 2023-02-07 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("result", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tendencies",
            options={"verbose_name": "Tendency", "verbose_name_plural": "Tendencies"},
        ),
        migrations.AddField(
            model_name="result",
            name="count",
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="kind",
            name="tendency",
            field=models.ManyToManyField(
                related_name="tendenc", to="result.tendencies"
            ),
        ),
        migrations.AlterField(
            model_name="result",
            name="mbti",
            field=models.CharField(
                choices=[
                    ("ENTJ", "ENTJ"),
                    ("ENTP", "ENTP"),
                    ("ENFJ", "ENFJ"),
                    ("ENFP", "ENFP"),
                    ("ESTJ", "ESTJ"),
                    ("ESTP", "ESTP"),
                    ("ESFJ", "ESFJ"),
                    ("ESFP", "ESFP"),
                    ("INTJ", "INTJ"),
                    ("INTP", "INTP"),
                    ("INFJ", "INFJ"),
                    ("INFP", "INFP"),
                    ("ISTJ", "ISFJ"),
                    ("ISTP", "ISTP"),
                    ("ISFJ", "ISFJ"),
                    ("ISFP", "ISFP"),
                ],
                max_length=4,
            ),
        ),
    ]
