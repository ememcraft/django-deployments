# Generated by Django 4.1.1 on 2023-01-27 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("firstName", models.CharField(max_length=192)),
                ("lastName", models.CharField(max_length=192, unique=True)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
