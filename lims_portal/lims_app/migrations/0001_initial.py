# Generated by Django 5.0.4 on 2024-06-17 17:35
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("name", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=255)),
                ("rack_number", models.CharField(max_length=50)),
                ("category", models.CharField(max_length=255)),
                ("quantity", models.IntegerField()),
                ("description", models.TextField()),
            ],
        ),
    ]