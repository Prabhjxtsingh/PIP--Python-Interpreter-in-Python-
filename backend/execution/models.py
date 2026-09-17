from django.db import models
from projects.models import Project

class ExecutionRun(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('RUNNING', 'Running'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='executions')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    exit_code = models.IntegerField(null=True, blank=True)
    stdout = models.TextField(blank=True)
    stderr = models.TextField(blank=True)
    duration_ms = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Run {self.id} for {self.project.name} ({self.status})"
