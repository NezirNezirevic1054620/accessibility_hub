from experience_expert.models import ExperienceExpert
from organization.models import Organization, Research
from rest_framework import serializers


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = (
            "id",
            "bedrijfsnaam",
            "type_bedrijf",
            "website",
            "beschrijving",
            "contactpersoon",
            "email",
            "telefoonnummer",
            "Overige_details",
        )


class ExperienceExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceExpert
        fields = (
            "id",
            "voornaam",
            "achternaam",
            "email",
            "postcode",
            "geslacht",
            "tel_nummer",
            "geboortedatum",
            "type_beperking",
            "gebruikte_hulpmiddelen",
            "bijzonderheden",
            "toezichthouder",
            "naam_voogd_toezichthouder",
            "email_voogd_toezichthouder",
            "tel_voogd_toezichthouder",
            "voorkeur_benadering",
            "type_onderzoek",
            "bijzonderheden_beschikbaarheid",
            "status",
        )


class ResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research
        fields = (
            "titel",
            "beschikbaar",
            "beschrijving",
            "datum_vanaf",
            "datum_tot",
            "type_onderzoek",
            "locatie",
            "met_beloning",
            "beloning",
            "doelgroep_leeftijd_van",
            "doelgroep_leeftijd_tot",
            "doelgroep_beperking",
        )
