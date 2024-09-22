from django.urls import path

from .views import OrganizationAPIView, ExperienceExpertAPIView, ResearchCreateView

urlpatterns = [
    path("organisations/", OrganizationAPIView.as_view()),
    path("experience_experts/", ExperienceExpertAPIView.as_view()),
    path("create_research/", ResearchCreateView.as_view()),
]
