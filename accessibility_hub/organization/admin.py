from django.contrib import admin

from .models import Organization


# Register your models here.


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = [
        "bedrijfsnaam",
        "type_bedrijf",
        "website",
        "beschrijving",
        "contactpersoon",
        "email",
        "telefoonnummer",
        "Overige_details",
    ]
