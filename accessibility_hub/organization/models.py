from django.db import models
from experience_expert.models import ExperienceExpert

# Create your models here.

type_bedrijf = (
    ("Commerciëel", "Commerciëel"),
    ("non-profit", "non-profit"),
)

status_keuzes = (
    ("goedgekeurd", "goedgekeurd"),
    ("afgekeurd", "afgekeurd"),
    ("in_behandeling", "in_behandeling"),
)


class Organization(models.Model):
    objects = models.Manager()
    bedrijfsnaam = models.CharField(max_length=255)
    type_bedrijf = models.CharField(max_length=255, choices=type_bedrijf)
    website = models.TextField()
    beschrijving = models.TextField()
    contactpersoon = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    telefoonnummer = models.CharField(max_length=255)
    Overige_details = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=status_keuzes, max_length=50)

    class Meta:
        db_table = "organization"


status = (
    ("nieuw", "nieuw"),
    ("goedgekeurd", "goedgekeurd"),
    ("afgekeurd", "afgekeurd"),
    ("gesloten", "gesloten"),
)

type_onderzoek = (
    ("locatie", "locatie"),
    ("telefonisch", "telefonisch"),
    ("online", "online"),
)

doelgroep_beperkingen = (
    (
        "Auditieve beperkingen",
        (
            ("Doof", "Doof"),
            ("Slechthorend", "Slechthorend"),
            ("Doofblind", "Doofblind"),
        ),
    ),
    (
        "Visuele beperkingen",
        (
            ("Blind", "Blind"),
            ("Slechtziend", "Slechtziend"),
            ("Kleurenblind", "Kleurenblind"),
            ("Doofblind", "Doofblind"),
        ),
    ),
    (
        "Motorische / lichamelijke beperkingen",
        (
            ("Amputatie en mismaaktheid", "Amputatie en mismaaktheid"),
            ("Artritus", "Artritus"),
            ("Fibromyalgie", "Fibromyalgie"),
            ("Reuma", "Reuma"),
            ("Verminderde handvaardigheid", "Verminderde handvaardigheid"),
            ("Spierdystrofie", "Spierdystrofie"),
            ("RSI", "RSI"),
            ("Tremor en Spasmen", "Tremor en Spasmen"),
            ("Quadriplegie of tetraplegie", " Quadriplegie of tetraplegie"),
        ),
    ),
    (
        "Cognitieve / neurologische beperkingen",
        (
            ("ADHD", "ADHD"),
            ("Autisme", "Autisme"),
            ("Leerstoornis", "Leerstoornis"),
            ("Geheugen beperking", "Geheugen beperking"),
            ("Multiple Sclerose", "Multiple Sclerose"),
            ("Epilepsie", "Epilepsie"),
            ("Migraine", "Migraine"),
        ),
    ),
)


class Research(models.Model):
    objects = models.Manager()
    titel = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=status, default="nieuw")
    beschikbaar = models.BooleanField(max_length=1, default=0)
    beschrijving = models.TextField()
    datum_vanaf = models.DateTimeField()
    datum_tot = models.DateTimeField()
    type_onderzoek = models.CharField(max_length=255, choices=type_onderzoek)
    locatie = models.TextField(null=True)
    met_beloning = models.BooleanField(max_length=1, default=0)
    beloning = models.TextField(null=True)
    doelgroep_leeftijd_van = models.IntegerField()
    doelgroep_leeftijd_tot = models.IntegerField()
    doelgroep_beperking = models.CharField(max_length=255, choices=doelgroep_beperkingen)
    ervaringsdeskundige = models.ForeignKey(
        ExperienceExpert, to_field="email", null=True, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "research"
