import pytest
from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
# Create your tests here.

client = APIClient()

@pytest.mark.django_db
def test_register():
    user_data = {
        "username": "Manikandanmkvk",
        "password": "12345678",
        "email": "manikandan@gmail.com"
    }
    url = reverse('register')
    response = client.post(url, user_data)

    assert response.status_code == 201