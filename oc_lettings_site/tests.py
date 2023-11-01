import pytest

from django.urls import reverse, resolve
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


@pytest.fixture
def client():
    client = Client()

    return client


@pytest.mark.django_db
class TestOCLettingsSiteUrls:
    def test_index_url(self):
        path = reverse("index")

        assert path == "/"
        assert resolve(path).view_name == "index"

    def test_admin_url(self):
        path = reverse("admin:index")

        assert path == "/admin/"
        assert resolve(path).view_name == "admin:index"


@pytest.mark.django_db
class TestOCLettingsSiteViews:
    def test_index_view(self, client):
        path = reverse("index")
        response = client.get(path)
        content = response.content.decode()

        expected_content = "Orange County Lettings 2023"

        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, "index.html")


def test_dummy():
    assert 1
