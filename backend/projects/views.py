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

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http import FileResponse, Http404
import os
from django.conf import settings

@api_view(['GET'])
@permission_classes([AllowAny])
def download_desktop_app(request):
    # In a real scenario, you'd probably zip the dist directory or point to an S3 URL.
    # For this scaffold, we'll assume the zip is placed in the media root.
    file_path = os.path.join(settings.MEDIA_ROOT, 'downloads', 'PIP_IDE.zip')
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='PIP_IDE.zip')
    raise Http404("Desktop app not found")
