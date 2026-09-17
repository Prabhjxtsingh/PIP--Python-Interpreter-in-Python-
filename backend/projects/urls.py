from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, ProjectFileViewSet, download_desktop_app

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'files', ProjectFileViewSet, basename='projectfile')

urlpatterns = [
    path('', include(router.urls)),
    path('download-desktop/', download_desktop_app, name='download-desktop'),
]
