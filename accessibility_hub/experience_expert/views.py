from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views import generic
from organization.models import Research

from .forms import ExperienceExpertForm, LoginForm
from .models import ExperienceExpert


class Login(generic.View):
    form_class = LoginForm
    template_name = "experience_expert_login.jinja"

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, context={"form": form})

    def post(self, request):
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                request.session["password"] = user.password
                request.session["username"] = user.username
                request.session["email"] = user.email

                response = redirect("/experience_expert")
                return response

            else:
                messages.success(
                    request,
                    message="Uw gebruikersnaam of wachtwoord is onjuist, probeer het opnieuw",
                )
                return redirect("login")

        else:
            return render(request, self.template_name, context={})


class Logout(generic.View):

    def get(self, request):
        logout(request)
        return redirect("index")


class Create(generic.CreateView, SuccessMessageMixin):
    form_class = ExperienceExpertForm
    template_name = "add.jinja"
    model = ExperienceExpert

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, context={"form": form})

    def post(self, request, *args, **kwargs):
        form = ExperienceExpertForm(request.POST)
        if form.is_valid():
            voornaam = request.POST["voornaam"]
            achternaam = request.POST["achternaam"]
            email = request.POST["email"]

            experience_expert = form.save()
            experience_expert.save()

            subject = "Ervaringsdeskundige registratie"
            html_message = render_to_string(
                template_name="email.html",
                context={"voornaam": voornaam, "achternaam": achternaam, "email": email},
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


class Search(generic.ListView):
    model = Research
    template_name = "experience_admin.jinja"
    context_object_name = "search_results"

    def get_queryset(self):
        result = super(Search, self).get_queryset()
        query = self.request.GET.get("search")
        if query:
            search_result = Research.objects.filter(titel__contains=query)
            result = search_result
        else:
            result = None
        return result


class ResearchView(generic.ListView):
    paginate_by = 10
    login_required = True
    model = Research
    template_name = "experience_admin.jinja"
    context_object_name = "object_list"

    def get_queryset(self):
        return Research.objects.filter(status="goedgekeurd")


class ViewResearch(generic.DetailView):
    model = Research
    template_name = "view_research.jinja"
    slug_field = "id"
    slug_url_kwarg = "id"


class CancelResearch(generic.UpdateView):
    model = Research
    template_name = "view_research.jinja"

    def post(self, request, *args, **kwargs):
        email = request.session["email"]
        if request.method == "POST":
            research_id = request.POST["id"]
            research = Research.objects.filter(id=research_id)
            selected_research = Research.objects.filter(id=research_id).values_list()
            selected_user = User.objects.filter(email=email).values_list()
            voornaam = selected_user[0][5]
            achternaam = selected_user[0][6]
            for research in research:
                print(research.titel)
            onderzoek = selected_research[0][1]
            Research.objects.filter(pk=research_id).update(ervaringsdeskundige=None)

            subject = "Uitschrijving onderzoek"
            html_message = render_to_string(
                template_name="cancel_mail.html",
                context={
                    "voornaam": voornaam,
                    "achternaam": achternaam,
                    "onderzoek": onderzoek,
                    "email": email,
                },
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
                message="U bent succesvol uitgeschreven voor het onderzoek, we hebben een bevestigingsmail "
                "gestuurd",
            )
        return render(request, self.template_name, context={"research": research})


class AcceptResearch(generic.UpdateView):
    model = Research
    template_name = "view_research.jinja"

    def post(self, request, *args, **kwargs):
        email = request.session["email"]
        if request.method == "POST":
            research_id = request.POST["id"]
            research = Research.objects.filter(id=research_id)
            selected_research = Research.objects.filter(id=research_id).values_list()
            selected_user = User.objects.filter(email=email).values_list()
            voornaam = selected_user[0][5]
            achternaam = selected_user[0][6]
            for research in research:
                print(research.titel)
            onderzoek = selected_research[0][1]
            Research.objects.filter(pk=research_id).update(ervaringsdeskundige=email)

            subject = "Onderzoeksacceptatie"
            html_message = render_to_string(
                template_name="acceptation_mail.html",
                context={
                    "voornaam": voornaam,
                    "achternaam": achternaam,
                    "onderzoek": onderzoek,
                    "email": email,
                },
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
                message="U bent succesvol aangemeld voor het onderzoek, we hebben een bevestigingsmail "
                "gestuurd",
            )
        return render(request, self.template_name, context={"research": research})


class ProfileView(generic.DetailView):
    template_name = "experience_expert_profile.jinja"
    model = User

    def get(self, request, *args, **kwargs):
        email = request.session["email"]
        profile = ExperienceExpert.objects.all().filter(email=email)
        return render(request, self.template_name, context={"profile": profile})


class ExperienceExpertDashboard(generic.ListView):
    model = ExperienceExpert
    template_name = "experience_admin_dashboard.jinja"

    def get(self, request, *args, **kwargs):
        researches = Research.objects.filter(status="goedgekeurd")

        return render(request, self.template_name, context={"researches": researches})
