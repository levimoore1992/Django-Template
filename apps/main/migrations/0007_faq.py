# Generated by Django 4.2.7 on 2024-02-06 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_socialmedialink"),
    ]

    operations = [
        migrations.CreateModel(
            name="FAQ",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.TextField()),
                ("answer", models.TextField()),
            ],
            options={
                "verbose_name": "FAQ",
                "verbose_name_plural": "FAQs",
            },
        ),
    ]
