from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views import generic
from django.urls import reverse
from experience_expert.models import ExperienceExpert
from organization.forms import UpdateResearchAdmin
from organization.models import Research, Organization
from organization.forms import RegisterOrganizationForm, UpdateOrganizationForm
from organization.models import Research
from organization.forms import UpdateResearchAdmin, Organization, Research
from organization.models import Research, Organization


from .forms import ExperienceExpertUpdateForm, LoginForm
from .utils import password_generator, username_generator


class Login(generic.View):
    form_class = LoginForm
    template_name = "login.jinja"

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

                response = redirect("/admin_hub")
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


@login_required()
def update_experience_expert(request, id):
    instance = get_object_or_404(ExperienceExpert, id=id)
    form = ExperienceExpertUpdateForm(request.POST or None, instance=instance)
    if form.is_valid():
        voornaam = request.POST["voornaam"]
        achternaam = request.POST["achternaam"]
        status = request.POST["status"]
        email = request.POST["email"]

        naam = str(voornaam) + str(achternaam)

        if status == "goedgekeurd":
            username = username_generator(naam)
            password = password_generator()
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=voornaam,
                last_name=achternaam,
            )
            user.save()

            subject = "Uw verzoek is goedgekeurd!"
            html_message = render_to_string(
                template_name="confirmation_email.html",
                context={
                    "voornaam": voornaam,
                    "achternaam": achternaam,
                    "email": email,
                    "username": username,
                    "password": password,
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
        elif status == "afgekeurd":
            subject = "Uw verzoek is afgekeurd"
            html_message = render_to_string(
                template_name="declination_email.html",
                context={
                    "voornaam": voornaam,
                    "achternaam": achternaam,
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
        form.save()
        return HttpResponseRedirect("/admin_hub")
    return render(request, template_name="update_expert.jinja", context={"form": form})


@login_required()
def research_view(request):
    return render(request, "research.jinja")


def bedrijven(request):
    organizations = Organization.objects.all()
    return render(request, "bedrijven.jinja", {"organizations": organizations})


def filtered_bedrijven(request, status):
    organizations = Organization.objects.filter(status=status)
    return render(request, "bedrijven.jinja", {"organizations": organizations})


def get_organisations(request, status):
    if status == "alles":
        organization = list(Organization.objects.values())
    else:
        organization = list(Organization.objects.filter(status=status).values())
    return JsonResponse(organization, safe=False)


def get_researchs(request, status):
    if status == "alles":
        researchs = list(Research.objects.values())
    else:
        researchs = list(Research.objects.filter(status=status).values())
    return JsonResponse(researchs, safe=False)


@login_required()
def update_research_view(request, id):
    form = UpdateResearchAdmin
    the_research = Research.objects.get(id=id)
    return render(request, "update_research.jinja", {"research": the_research, "form": form})


@login_required()
def update_research_status(request, id):
    status = request.POST["status"]
    Research.objects.filter(id=id).update(status=status)
    return redirect("researches")


@login_required()
def update_organization_status(request, id):
    status = request.POST["status"]
    Organization.objects.filter(id=id).update(status=status)
    return redirect("organizations")


@login_required()
def admin(request):
    experience_experts = ExperienceExpert.objects.all()
    return render(
        request, template_name="admin.jinja", context={"experience_experts": experience_experts}
    )


@login_required
def update_organization_status(request, id):
    organization = get_object_or_404(Organization, id=id)

    if request.method == "POST":
        form = UpdateOrganizationForm(request.POST, instance=organization)

        if form.is_valid():

            organization.status = form.cleaned_data["status"]
            organization.save()
            return redirect("bedrijven")
        else:
            return render(
                request, "update_organizations.jinja", {"organization": organization, "form": form}
            )
    else:
        form = UpdateOrganizationForm(instance=organization)

    return render(
        request, "update_organizations.jinja", {"organization": organization, "form": form}
    )


class SearchExperienceExpert(generic.ListView):
    model = ExperienceExpert
    template_name = "experience_experts.jinja"
    context_object_name = "search_results"

    def get_queryset(self):
        result = super(SearchExperienceExpert, self).get_queryset()
        query = self.request.GET.get("search")
        if query:
            search_result = ExperienceExpert.objects.filter(voornaam__contains=query)
            result = search_result
        else:
            result = None
        return result


class SearchOrganization(generic.ListView):
    model = Organization
    template_name = "bedrijven.jinja"
    context_object_name = "search_results"

    def get_queryset(self):
        result = super(SearchOrganization, self).get_queryset()
        query = self.request.GET.get("search")
        if query:
            search_result = Organization.objects.filter(bedrijfsnaam__contains=query)
            result = search_result
        else:
            result = None
        return result


class ExperienceExpertView(generic.ListView):
    paginate_by = 10
    login_required = True
    model = ExperienceExpert
    template_name = "experience_experts.jinja"

    def get_experts(request):
        experts = list(ExperienceExpert.objects.values())
        return JsonResponse(experts, safe=False)


class OrganizationView(generic.ListView):
    model = Organization
    template_name = "bedrijven.jinja"
    paginate_by = 10


class ProfileView(generic.DetailView):
    template_name = "admin_profile.jinja"
    model = User

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})


class AdminDashboard(generic.ListView):
    model = ExperienceExpert
    template_name = "admin_dashboard.jinja"

    def get(self, request, *args, **kwargs):
        experience_experts = ExperienceExpert.objects.all()
        organisations = Organization.objects.all()
        researches = Research.objects.all()

        return render(
            request,
            self.template_name,
            context={
                "experience_experts": experience_experts,
                "organisations": organisations,
                "researches": researches,
            },
        )
