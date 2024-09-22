from django.db import models

# Create your models here.

beperking_keuzes = (
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
    ("Verminderde handvaardigheid", "Verminderde handvaardigheid"),
    ("Spierdystrofie", "Spierdystrofie"),
    ("RSI", "RSI"),
    ("Tremor en Spasmen", "Tremor en Spasmen"),
    ("Quadriplegie of tetraplegie", "Quadriplegie of tetraplegie"),
    ("ADHD", "ADHD"),
    ("Autisme", "Autisme"),
    ("Leerstoornis", "Leerstoornis"),
    ("Geheugen beperking", "Geheugen beperking"),
    ("Multiple Sclerose", "Multiple Sclerose"),
    ("Epilepsie", "Epilepsie"),
    ("Migraine", "Migraine"),
)

voorkeur_keuzes = (
    ("telefonisch", "telefonisch"),
    ("email", "email"),
)

onderzoek_keuzes = (
    ("telefonisch", "telefonisch"),
    ("internet", "internet"),
    ("locatie", "locatie"),
)

geslacht = (("man", "man"), ("vrouw", "vrouw"), ("anders", "anders"))

status_keuzes = (
    ("goedgekeurd", "goedgekeurd"),
    ("afgekeurd", "afgekeurd"),
    ("in_behandeling", "in_behandeling"),
)


class ExperienceExpert(models.Model):
    objects = models.Manager()

    voornaam = models.CharField(
        max_length=255,
    )
    achternaam = models.CharField(max_length=255)
    postcode = models.CharField(max_length=6)
    geslacht = models.CharField(max_length=40, choices=geslacht)
    email = models.EmailField(max_length=255)
    tel_nummer = models.CharField(max_length=15)
    geboortedatum = models.DateField()
    type_beperking = models.CharField(max_length=100, choices=beperking_keuzes)
    gebruikte_hulpmiddelen = models.TextField(max_length=255)
    bijzonderheden = models.TextField(max_length=255)
    toezichthouder = models.BooleanField(default=1)
    status = models.CharField(choices=status_keuzes, max_length=50, default="in_behandeling")
    naam_voogd_toezichthouder = models.CharField(max_length=255)
    email_voogd_toezichthouder = models.EmailField(max_length=255)
    tel_voogd_toezichthouder = models.CharField(max_length=255)
    voorkeur_benadering = models.CharField(choices=voorkeur_keuzes, max_length=40)
    type_onderzoek = models.CharField(choices=onderzoek_keuzes, max_length=40)
    bijzonderheden_beschikbaarheid = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return self.type_beperking

    class Meta:
        db_table = "experience_expert_update"
