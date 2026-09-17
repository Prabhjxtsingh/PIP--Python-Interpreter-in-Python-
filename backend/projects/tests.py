import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from accounts.models import User
from projects.models import Project

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='password123')

@pytest.mark.django_db
def test_create_project(api_client, user):
    api_client.force_authenticate(user=user)
    url = reverse('project-list')
    response = api_client.post(url, {'name': 'Test Project', 'description': 'A test project'})
    
    assert response.status_code == 201
    assert Project.objects.count() == 1
    assert Project.objects.get().name == 'Test Project'

@pytest.mark.django_db
def test_list_projects(api_client, user):
    Project.objects.create(name='Project 1', owner=user)
    Project.objects.create(name='Project 2', owner=user)
    
    api_client.force_authenticate(user=user)
    url = reverse('project-list')
    response = api_client.get(url)
    
    assert response.status_code == 200
    assert len(response.data) == 2
