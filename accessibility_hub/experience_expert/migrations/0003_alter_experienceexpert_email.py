# Generated by Django 4.2.9 on 2024-03-06 18:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("experience_expert", "0002_experienceexpert_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="experienceexpert",
            name="email",
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
