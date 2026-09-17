from rest_framework import viewsets, parsers
from rest_framework.permissions import IsAuthenticated
from .models import Project, ProjectFile
from .serializers import ProjectSerializer, ProjectFileSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProjectFileViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectFileSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    def get_queryset(self):
        return ProjectFile.objects.filter(project__owner=self.request.user)
