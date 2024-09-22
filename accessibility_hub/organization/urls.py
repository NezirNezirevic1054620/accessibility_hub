from django.urls import path

from . import views

urlpatterns = [
    path("create", views.RegisterOrganization.as_view(), name="create"),
    path("form-research", views.formResearch, name="formResearch"),
    path("create-research", views.createResearch, name="createResearch"),
]
