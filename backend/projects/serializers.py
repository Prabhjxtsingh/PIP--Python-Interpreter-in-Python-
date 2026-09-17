from rest_framework import serializers
from .models import Project, ProjectFile

class ProjectFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectFile
        fields = ['id', 'file', 'relative_path', 'is_directory', 'created_at']

class ProjectSerializer(serializers.ModelSerializer):
    files = ProjectFileSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'owner', 'created_at', 'files']
        read_only_fields = ['owner']
