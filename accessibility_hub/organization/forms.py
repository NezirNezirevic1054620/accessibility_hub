from django import forms
from django.forms import ModelForm
from .models import Organization, Research


class RegisterOrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = [
            "bedrijfsnaam",
            "type_bedrijf",
            "website",
            "beschrijving",
            "contactpersoon",
            "email",
            "telefoonnummer",
            "Overige_details",
        ]
        error_messages = {
            "bedrijfsnaam": {
                "required": "Dit veld is verplicht",
            },
            "type_bedrijf": {
                "required": "Dit veld is verplicht.",
            },
            "website": {
                "required": "Dit veld is verplicht",
            },
            "beschrijving": {
                "required": "Dit veld is verplicht.",
            },
            "contactpersoon": {
                "required": "Dit veld is verplicht",
            },
            "email": {
                "required": "Dit veld is verplicht.",
            },
            "telefoonnummer": {
                "required": "Dit veld is verplicht.",
            },
            "Overige_details": {
                "required": "Dit veld is verplicht.",
            },
        }

        widgets = {
            "bedrijfsnaam": forms.TextInput(
                attrs={
                    "placeholder": "Voer in uw bedrijfsnaam",
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "type_bedrijf": forms.Select(
                attrs={
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300"
                }
            ),
            "website": forms.TextInput(
                attrs={
                    "placeholder": "Voer in uw website",
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "beschrijving": forms.Textarea(
                attrs={
                    "placeholder": "Voer in uw bedrijfsbeschrijving",
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "contactpersoon": forms.TextInput(
                attrs={
                    "placeholder": "Voer een contacpersoon in",
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Voer in uw email",
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "telefoonnummer": forms.TextInput(
                attrs={
                    "placeholder": "Voer in uw telefoonnummer",
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "status": forms.Select(
                attrs={
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "Overige_details": forms.Textarea(
                attrs={
                    "placeholder": "Voer in overige details",
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
        }


class UpdateOrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = [
            "bedrijfsnaam",
            "type_bedrijf",
            "website",
            "beschrijving",
            "contactpersoon",
            "email",
            "telefoonnummer",
            "Overige_details",
            "status",
        ]

        widgets = {
            "bedrijfsnaam": forms.TextInput(
                attrs={
                    "placeholder": "Voer in uw bedrijfsnaam",
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "type_bedrijf": forms.Select(
                attrs={
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300"
                }
            ),
            "website": forms.TextInput(
                attrs={
                    "placeholder": "Voer in uw website",
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "beschrijving": forms.Textarea(
                attrs={
                    "placeholder": "Voer in uw bedrijfsbeschrijving",
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "contactpersoon": forms.TextInput(
                attrs={
                    "placeholder": "Voer een contacpersoon in",
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Voer in uw email",
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "telefoonnummer": forms.TextInput(
                attrs={
                    "placeholder": "Voer in uw telefoonnummer",
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "Overige_details": forms.Textarea(
                attrs={
                    "placeholder": "Voer in overige details",
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "status": forms.Select(
                attrs={
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
        }


class createResearchForm(ModelForm):

    class Meta:
        model = Research
        fields = [
            "titel",
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
        ]

        widgets = {
            "titel": forms.TextInput(
                attrs={
                    "placeholder": "Voer in uw bedrijfsnaam",
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "beschrijving": forms.Textarea(
                attrs={
                    "placeholder": "Voer in uw bedrijfsbeschrijving",
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "datum_vanaf": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                    "id": "startDate",
                    "type": "date",
                },
            ),
            "datum_tot": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={
                    "placeholder": "Voer een contacpersoon in",
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                    "id": "endDate",
                    "type": "date",
                    "disabled": True,
                },
            ),
            "type_onderzoek": forms.Select(
                attrs={
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                    "id": "typeResearch",
                }
            ),
            "locatie": forms.TextInput(
                attrs={
                    "placeholder": "Locatie",
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                    "id": "location",
                    "disabled": True,
                }
            ),
            "met_beloning": forms.CheckboxInput(
                attrs={
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                    "id": "showReward",
                }
            ),
            "beloning": forms.Textarea(
                attrs={
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                    "id": "reward",
                    "disabled": True,
                }
            ),
            "doelgroep_leeftijd_van": forms.NumberInput(
                attrs={
                    "min": "0",
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "doelgroep_leeftijd_tot": forms.NumberInput(
                attrs={
                    "min": "0",
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "doelgroep_beperking": forms.Select(
                attrs={
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
        }


class UpdateResearchAdmin(ModelForm):

    class Meta:
        model = Research
        fields = [
            "status",
        ]

        widgets = {
            "status": forms.Select(
                attrs={
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
        }
