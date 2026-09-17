from django.db import models
from django.conf import settings

class Project(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.owner.username})"

class ProjectFile(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='project_files/', null=True, blank=True)
    relative_path = models.CharField(max_length=1024, help_text="Path relative to the project root (e.g., 'src/main.py')")
    is_directory = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.project.name} - {self.relative_path}"
