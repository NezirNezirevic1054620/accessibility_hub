from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path("", views.AdminDashboard.as_view(), name="admin_dashboard"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("update/<int:id>", views.update_experience_expert, name="update"),
    path("", views.admin, name="admin"),
    path("research/", views.research_view, name="research"),
    path("get_researchs/<str:status>", views.get_researchs, name="get_researchs"),
    path(
        "experience_experts/",
        login_required(views.ExperienceExpertView.as_view()),
        name="experience_experts",
    ),
    path("get_experts", views.ExperienceExpertView.get_experts, name="get_experts"),
    path("researches/", views.research_view, name="researches"),
    path("get_researches/<str:status>", views.get_researchs, name="get_researchs"),
    path("update-research/<int:id>", views.update_research_view, name="update_research_view"),
    path(
        "search_experience_expert/",
        login_required(views.SearchExperienceExpert.as_view()),
        name="search_experience_experts",
    ),
    path(
        "search_organization/",
        login_required(views.SearchOrganization.as_view()),
        name="search_organization",
    ),
    path("organizations/", login_required(views.OrganizationView.as_view()), name="organizations"),
    path(
        "update-researchstatus/<int:id>",
        views.update_research_status,
        name="update_research_status",
    ),
    path(
        "update_organization_status/<int:id>/",
        views.update_organization_status,
        name="update_organization_status",
    ),
    path("bedrijven/", views.bedrijven, name="bedrijven"),
    path("get-organizations/<str:status>", views.get_organisations, name="get_organisations"),
    path("bedrijven/<str:status>/", views.filtered_bedrijven, name="filtered_bedrijven"),
    path("profile/<int:pk>/", login_required(views.ProfileView.as_view()), name="profile_admin"),
]
