# Generated by Django 4.2.9 on 2024-01-28 14:04

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ExperienceExpert",
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
                ("voornaam", models.CharField(max_length=255)),
                ("achternaam", models.CharField(max_length=255)),
                ("postcode", models.CharField(max_length=6)),
                ("geslacht", models.CharField(max_length=40)),
                ("email", models.EmailField(max_length=255)),
                ("tel_nummer", models.CharField(max_length=15)),
                ("geboortedatum", models.DateField()),
                (
                    "type_beperking",
                    models.CharField(
                        choices=[
                            ("Doof", "Doof"),
                            ("Slechthorend", "Slechthorend"),
                            ("Doofblind", "Doofblind"),
                            ("Blind", "Blind"),
                            ("Slechtziend", "Slechtziend"),
                            ("Kleurenblind", "Kleurenblind"),
                            ("Doofblind", "Doofblind"),
                            ("Amputatie en mismaaktheid", "Amputatie en mismaaktheid"),
                            ("Artritus", "Artritus"),
                            ("Fibromyalgie", "Fibromyalgie"),
                            ("Reuma", "Reuma"),
                            (
                                "Verminderde handvaardigheid",
                                "Verminderde handvaardigheid",
                            ),
                            ("Spierdystrofie", "Spierdystrofie"),
                            ("RSI", "RSI"),
                            ("Tremor en Spasmen", "Tremor en Spasmen"),
                            (
                                "Quadriplegie of tetraplegie",
                                "Quadriplegie of tetraplegie",
                            ),
                            ("ADHD", "ADHD"),
                            ("Autisme", "Autisme"),
                            ("Leerstoornis", "Leerstoornis"),
                            ("Geheugen beperking", "Geheugen beperking"),
                            ("Multiple Sclerose", "Multiple Sclerose"),
                            ("Epilepsie", "Epilepsie"),
                            ("Migraine", "Migraine"),
                        ],
                        max_length=100,
                    ),
                ),
                ("gebruikte_hulpmiddelen", models.TextField(max_length=255)),
                ("bijzonderheden", models.TextField(max_length=255)),
                ("toezichthouder", models.BooleanField(default=1)),
                ("naam_voogd_toezichthouder", models.CharField(max_length=255)),
                ("email_voogd_toezichthouder", models.EmailField(max_length=255)),
                ("tel_voogd_toezichthouder", models.CharField(max_length=255)),
                (
                    "voorkeur_benadering",
                    models.CharField(
                        choices=[("telefonisch", "telefonisch"), ("email", "email")],
                        max_length=40,
                    ),
                ),
                (
                    "type_onderzoek",
                    models.CharField(
                        choices=[
                            ("telefonisch", "telefonisch"),
                            ("internet", "internet"),
                            ("locatie", "locatie"),
                        ],
                        max_length=40,
                    ),
                ),
                ("bijzonderheden_beschikbaarheid", models.TextField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "experience_expert",
            },
        ),
    ]
