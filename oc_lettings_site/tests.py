import pytest

from django.urls import reverse, resolve
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


@pytest.fixture
def client():
    """Fixture to create a test client."""
    client = Client()

    return client


@pytest.mark.django_db
class TestOCLettingsSiteUrls:
    """Class grouping URL tests of the oc_lettings_site application."""
    def test_index_url(self):
        """
        GIVEN a URL path for the index is expected,
        WHEN the URL path is retrieved and the view name is resolved,
        THEN it should match the expected path and view name.
        """
        path = reverse("index")

        assert path == "/"
        assert resolve(path).view_name == "index"

    def test_admin_url(self):
        """
        GIVEN a URL path for the admin index is expected,
        WHEN the URL path is retrieved and the view name is resolved,
        THEN it should match the expected path and view name.
        """
        path = reverse("admin:index")

        assert path == "/admin/"
        assert resolve(path).view_name == "admin:index"


@pytest.mark.django_db
class TestOCLettingsSiteViews:
    """Class grouping view tests of the oc_lettings_site application."""
    def test_index_view(self, client):
        """
        GIVEN a client for the index view,
        WHEN the view is accessed,
        THEN it should render with the expected content, status code, and template.
        """
        path = reverse("index")
        response = client.get(path)
        content = response.content.decode()

        expected_content = "Orange County Lettings 2023"

        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, "index.html")

    def test_404_view(self, client):
        """
        GIVEN a client for an unexisting profile view,
        WHEN the view is accessed,
        THEN it should render with the expected content, status code, and template.
        """
        path = reverse("profiles:profile", kwargs={"username": "azazeaze"})
        response = client.get(path)
        content = response.content.decode()

        expected_content = "404 - Page not found"

        assert expected_content in content
        assert response.status_code == 404
        assertTemplateUsed(response, "404.html")


def test_dummy():
    """Dummy test which was part of the initial repository."""
    assert 1
