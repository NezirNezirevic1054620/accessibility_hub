from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.Create.as_view(), name="create"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("view_researches/", login_required(views.ResearchView.as_view()), name="view_researches"),
    path("search/", login_required(views.Search.as_view()), name="search"),
    path(
        "",
        login_required(views.ExperienceExpertDashboard.as_view()),
        name="experience_expert_dashboard",
    ),
    path(
        "'view_research/<slug:id>/'", login_required(views.ViewResearch.as_view()), name="research"
    ),
    path(
        "accept_research/", login_required(views.AcceptResearch.as_view()), name="accept_research"
    ),
    path(
        "cancel_research/", login_required(views.CancelResearch.as_view()), name="cancel_research"
    ),
    path("profile/<int:pk>/", login_required(views.ProfileView.as_view()), name="profile"),
]
