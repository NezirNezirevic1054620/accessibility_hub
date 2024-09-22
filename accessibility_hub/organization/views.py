from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views import generic

from .models import Organization, Research
from .forms import RegisterOrganizationForm, createResearchForm


# Create your views here.
class RegisterOrganization(generic.CreateView, SuccessMessageMixin):
    form_class = RegisterOrganizationForm
    template_name = "create.jinja"
    model = Organization

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, context={"form": form})

    def post(self, request, *args, **kwargs):
        form = RegisterOrganizationForm(request.POST)
        if form.is_valid():
            bedrijfsnaam = request.POST["bedrijfsnaam"]
            contactpersoon = request.POST["contactpersoon"]
            email = request.POST["email"]

            organization = form.save()
            organization.save()

            subject = "Organisatie registratie"
            html_message = render_to_string(
                template_name="organization_confirmation_mail.html",
                context={"bedrijfsnaam": bedrijfsnaam, "contactpersoon": contactpersoon},
            )
            plain_message = strip_tags(html_message)
            from_email = "django@mailtrap.club"
            to = email
            send_mail(
                subject=subject,
                message=plain_message,
                from_email=from_email,
                recipient_list=[to],
                html_message=html_message,
            )

            messages.success(
                request,
                message="Uw formulier is succesvol verzonden, check uw email voor een bevestiging",
            )

            return render(request, self.template_name, context={"form": form})
        else:
            messages.error(
                request,
                message="Er ging iets mis, uw formulier kon niet worden verzonde, probeer later opnieuw",
            )
            return render(request, self.template_name, context={"form": form})


def formResearch(request):
    form = createResearchForm
    return render(request, "createResearch.jinja", {"form": form})


def createResearch(request):
    titel = request.POST["titel"]
    beschrijving = request.POST["beschrijving"]
    datum_vanaf = request.POST["datum_vanaf"]
    datum_tot = request.POST["datum_tot"]
    locatie = "" if "locatie" not in request.POST else request.POST["locatie"]
    met_beloning = 0 if "met_beloning" not in request.POST else 1
    beloning = "" if "beloning" not in request.POST else request.POST["beloning"]
    doelgroep_leeftijd_van = request.POST["doelgroep_leeftijd_van"]
    doelgroep_leeftijd_tot = request.POST["doelgroep_leeftijd_tot"]
    doelgroep_beperking = request.POST["doelgroep_beperking"]
    print(request.POST, locatie)
    researchData = Research(
        titel=titel,
        beschrijving=beschrijving,
        datum_vanaf=datum_vanaf,
        datum_tot=datum_tot,
        locatie=locatie,
        met_beloning=met_beloning,
        beloning=beloning,
        doelgroep_leeftijd_van=doelgroep_leeftijd_van,
        doelgroep_leeftijd_tot=doelgroep_leeftijd_tot,
        doelgroep_beperking=doelgroep_beperking,
    )
    researchData.save()
    return redirect("/")
