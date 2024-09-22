from experience_expert.models import ExperienceExpert
from organization.models import Organization
from rest_framework import generics, permissions

from .serializers import OrganizationSerializer, ExperienceExpertSerializer, ResearchSerializer


class OrganizationAPIView(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class ExperienceExpertAPIView(generics.ListAPIView):
    queryset = ExperienceExpert.objects.all()
    serializer_class = ExperienceExpertSerializer


class ResearchCreateView(generics.CreateAPIView):
    serializer_class = ResearchSerializer
    permission_classes = [permissions.AllowAny]
