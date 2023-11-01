import pytest

from django.urls import reverse, resolve
from django.test import Client
from django.contrib.auth.models import User
from profiles.models import Profile
from pytest_django.asserts import assertTemplateUsed


@pytest.fixture
def user_fixture():
    """Fixture to create a User object."""
    username = "Pikachu42"
    first_name = "Alex"
    last_name = "Terieur"
    email = "alex.terieur@pokemon.com"

    user = User.objects.create(username=username,
                               first_name=first_name,
                               last_name=last_name,
                               email=email)

    return user


@pytest.fixture
def user_fixture2():
    """Fixture to create another User object."""
    username = "Tortank"
    first_name = "Sarah"
    last_name = "Croche"
    email = "sarah.croche@sav.com"

    user = User.objects.create(username=username,
                               first_name=first_name,
                               last_name=last_name,
                               email=email)

    return user


@pytest.fixture
def profile_fixture(user_fixture):
    """Fixture to create a Profile object."""
    user = user_fixture
    favorite_city = "Los Angeles"

    profile = Profile.objects.create(user=user,
                                     favorite_city=favorite_city)

    return profile


@pytest.fixture
def profile_fixture2(user_fixture2):
    """Fixture to create another Profile object."""
    user = user_fixture2
    favorite_city = "Paris"

    profile = Profile.objects.create(user=user,
                                     favorite_city=favorite_city)

    return profile


@pytest.fixture
def client():
    """Fixture to create a test client."""
    client = Client()

    return client


@pytest.mark.django_db
class TestProfilesUrls:
    """Class grouping URL tests of the Profiles application."""
    def test_profiles_index_url(self):
        """
        GIVEN a URL path for the profiles index is expected,
        WHEN the URL path is retrieved and the view name is resolved,
        THEN it should match the expected path and view name.
        """
        path = reverse("profiles:profiles_index")

        assert path == "/profiles/"
        assert resolve(path).view_name == "profiles:profiles_index"

    def test_profile_url(self, profile_fixture):
        """
        GIVEN a profile fixture and a URL path for a specific profile is expected,
        WHEN the URL path is retrieved and the view name is resolved,
        THEN it should match the expected path and view name.
        """
        path = reverse("profiles:profile", kwargs={"username": profile_fixture.user.username})

        assert path == f"/profiles/{profile_fixture.user.username}/"
        assert resolve(path).view_name == "profiles:profile"


@pytest.mark.django_db
class TestProfilesViews:
    """Class grouping view tests of the Profiles application."""
    def test_profiles_index_view(self, client, profile_fixture):
        """
        GIVEN a client for the profiles index view and a profile fixture,
        WHEN the view is accessed,
        THEN it should render with the expected content, status code, and template.
        """
        path = reverse("profiles:profiles_index")
        response = client.get(path)
        content = response.content.decode()

        expected_content = f"{profile_fixture.user.username}"

        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/index.html")

    def test_profile_view(self, client, profile_fixture):
        """
        GIVEN a client for a specific profile view and a profile fixture,
        WHEN the view is accessed,
        THEN it should render with the expected content, status code, and template.
        """
        path = reverse("profiles:profile", kwargs={"username": profile_fixture.user.username})
        response = client.get(path)
        content = response.content.decode()

        expected_content = f"{profile_fixture.user.first_name}"

        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/profile.html")


@pytest.mark.django_db
class TestProfilesModels:
    """Class grouping model tests of the Profiles application."""
    def test_user_model(self, user_fixture):
        """
        GIVEN a user fixture with specific user details,
        WHEN the user model method is called,
        THEN it should return the expected content.
        """
        expected_content = f'{user_fixture.first_name}'

        assert user_fixture.get_short_name() == expected_content

    def test_profile_model(self, profile_fixture):
        """
        GIVEN a profile fixture,
        WHEN the profile model method is called,
        THEN it should return the expected content.
        """
        expected_content = profile_fixture.user.username

        assert str(profile_fixture) == expected_content


@pytest.mark.django_db
class TestProfilesIntegration:
    """Class grouping integration tests of the Profiles application."""
    def test_two_profiles_creation_url_and_navigation(self,
                                                      client,
                                                      profile_fixture,
                                                      profile_fixture2):
        """
        GIVEN a client, profile fixtures, and specific URLs for profiles,
        WHEN the URLs are accessed,
        THEN they should render with the expected content, status code, and template.
        """
        path = reverse("profiles:profiles_index")
        response = client.get(path)
        content = response.content.decode()

        expected_content = profile_fixture.user.username
        expected_content2 = profile_fixture2.user.username

        assert expected_content in content
        assert expected_content2 in content
        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/index.html")

        path = reverse("profiles:profile", kwargs={"username": profile_fixture.user.username})
        response = client.get(path)
        content = response.content.decode()

        expected_content = profile_fixture.user.first_name

        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/profile.html")

        path = reverse("profiles:profile", kwargs={"username": profile_fixture2.user.username})
        response = client.get(path)
        content = response.content.decode()

        expected_content = profile_fixture2.user.first_name

        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/profile.html")
