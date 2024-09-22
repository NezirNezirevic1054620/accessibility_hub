from django.contrib import admin

from .models import ExperienceExpert


# Register your models here.
@admin.register(ExperienceExpert)
class ExperienceExpertAdmin(admin.ModelAdmin):
    list_display = [
        "voornaam",
        "achternaam",
        "postcode",
        "tel_nummer",
        "type_beperking",
        "created_at",
        "updated_at",
    ]
