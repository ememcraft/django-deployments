# Generated by Django 4.1.1 on 2023-01-27 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="lastName",
            field=models.CharField(max_length=192),
        ),
    ]
