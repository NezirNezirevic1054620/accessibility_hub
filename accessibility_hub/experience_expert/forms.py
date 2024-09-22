from datetime import date

from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import ExperienceExpert


class LoginForm(ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password"]


class ExperienceExpertForm(ModelForm):
    class Meta:
        model = ExperienceExpert
        fields = [
            "voornaam",
            "achternaam",
            "postcode",
            "geslacht",
            "email",
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
        ]
        error_messages = {
            "voornaam": {
                "required": "Dit veld is verplicht",
            },
            "achternaam": {
                "required": "Dit veld is verplicht.",
            },
            "postcode": {
                "required": "Dit veld is verplicht",
            },
            "geslacht": {
                "required": "Dit veld is verplicht.",
            },
            "email": {
                "required": "Dit veld is verplicht",
            },
            "tel_nummer": {
                "required": "Dit veld is verplicht.",
            },
            "geboortedatum": {
                "required": "Dit veld is verplicht",
            },
            "type_beperking": {
                "required": "Dit veld is verplicht.",
            },
            "gebruikte_hulpmiddelen": {
                "required": "Dit veld is verplicht.",
            },
            "bijzonderheden": {
                "required": "Dit veld is verplicht.",
            },
            "voorkeur_benadering": {
                "required": "Dit veld is verplicht.",
            },
            "type_onderzoek": {
                "required": "Dit veld is verplicht.",
            },
        }

        widgets = {
            "voornaam": forms.TextInput(
                attrs={
                    "placeholder": "Voer in uw voornaam",
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "achternaam": forms.TextInput(
                attrs={
                    "placeholder": "Voer in uw achternaam",
                    "class": "block mb-4 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg border "
                    "border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "postcode": forms.TextInput(
                attrs={
                    "placeholder": "Voer in uw postcode",
                    "class": "block mb-4 mt-2 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg "
                    "border border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "geslacht": forms.TextInput(
                attrs={
                    "placeholder": "Voer in uw geslacht",
                    "class": "block mb-4 mt-2 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg "
                    "border border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Voer in uw email",
                    "class": "block mb-4 mt-2 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg "
                    "border border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "tel_nummer": forms.TextInput(
                attrs={
                    "placeholder": "Voer uw telefoonnummer in",
                    "class": "block mb-4  mt-2 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg "
                    "border border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "geboortedatum": forms.SelectDateWidget(
                years=range(date.today().year, date.today().year - 100, -1),
                attrs={
                    "class": "block mb-4 mt-2 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg "
                    "border border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300"
                },
            ),
            "type_beperking": forms.Select(
                attrs={
                    "placeholder": "Voer in uw type beperking",
                    "class": "block mb-4 mt-2 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg "
                    "border border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "gebruikte_hulpmiddelen": forms.Textarea(
                attrs={
                    "placeholder": "Voer in uw gebruikte hulpmiddelen",
                    "class": "block mb-4 mt-2 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg "
                    "border border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "bijzonderheden": forms.Textarea(
                attrs={
                    "placeholder": "Voer in uw bijzonderheden",
                    "class": "block mb-4 mt-2 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg "
                    "border border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "toezichthouder": forms.CheckboxInput(
                attrs={
                    "type": "checkbox",
                    "class": "block mb-4 mt-2 placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg "
                    "border border-gray-300 bg-white px-5 py-4 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "naam_voogd_toezichthouder": forms.TextInput(
                attrs={
                    "placeholder": "Voer in namm van uw voogd of toezichthouder",
                    "class": "block mb-4 mt-2 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg "
                    "border border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "email_voogd_toezichthouder": forms.EmailInput(
                attrs={
                    "placeholder": "Voer in email van uw voogd of toezichthouder",
                    "class": "block mb-4 mt-2 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg "
                    "border border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "tel_voogd_toezichthouder": forms.TextInput(
                attrs={
                    "placeholder": "Voer in telefoonnummer van uw vogd of toezichthouder",
                    "class": "block mb-4 mt-2 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg "
                    "border border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
            "voorkeur_benadering": forms.Select(
                attrs={
                    "class": "block mb-4 mt-2 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg "
                    "border border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300"
                }
            ),
            "type_onderzoek": forms.Select(
                attrs={
                    "class": "block mb-4 mt-2 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg "
                    "border border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300"
                }
            ),
            "bijzonderheden_beschikbaarheid": forms.TextInput(
                attrs={
                    "placeholder": "Voer in bijzonderheden beschikbaarheid",
                    "class": "block mb-4 mt-2 w-full placeholder-gray-400/70 dark:placeholder-gray-500 rounded-lg "
                    "border border-gray-300 bg-white px-5 py-2.5 text-gray-700 focus:border-blue-400 "
                    "focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40 "
                    "dark:border-gray-600 dark:bg-gray-900 dark:text-gray-300 dark:focus:border-blue-300",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(ExperienceExpertForm, self).__init__(*args, **kwargs)
        self.fields["naam_voogd_toezichthouder"].required = False
        self.fields["email_voogd_toezichthouder"].required = False
        self.fields["tel_voogd_toezichthouder"].required = False
