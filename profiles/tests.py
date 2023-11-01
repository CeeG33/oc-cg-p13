import pytest

from django.urls import reverse, resolve
from django.test import Client
from django.contrib.auth.models import User
from profiles.models import Profile
from pytest_django.asserts import assertTemplateUsed


@pytest.fixture
def user_fixture():
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
    user = user_fixture
    favorite_city = "Los Angeles"

    profile = Profile.objects.create(user=user,
                                     favorite_city=favorite_city)

    return profile


@pytest.fixture
def profile_fixture2(user_fixture2):
    user = user_fixture2
    favorite_city = "Paris"

    profile = Profile.objects.create(user=user,
                                     favorite_city=favorite_city)

    return profile


@pytest.fixture
def client():
    client = Client()

    return client


@pytest.mark.django_db
class TestProfilesUrls:
    def test_profiles_index_url(self):
        path = reverse("profiles:profiles_index")

        assert path == "/profiles/"
        assert resolve(path).view_name == "profiles:profiles_index"

    def test_profile_url(self, profile_fixture):
        path = reverse("profiles:profile", kwargs={"username": profile_fixture.user.username})

        assert path == f"/profiles/{profile_fixture.user.username}/"
        assert resolve(path).view_name == "profiles:profile"


@pytest.mark.django_db
class TestProfilesViews:
    def test_profiles_index_view(self, client, profile_fixture):
        path = reverse("profiles:profiles_index")
        response = client.get(path)
        content = response.content.decode()

        expected_content = f"{profile_fixture.user.username}"

        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/index.html")

    def test_profile_view(self, client, profile_fixture):
        path = reverse("profiles:profile", kwargs={"username": profile_fixture.user.username})
        response = client.get(path)
        content = response.content.decode()

        expected_content = f"{profile_fixture.user.first_name}"

        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/profile.html")


@pytest.mark.django_db
class TestProfilesModels:
    def test_user_model(self, user_fixture):
        expected_content = f'{user_fixture.first_name}'

        assert user_fixture.get_short_name() == expected_content

    def test_profile_model(self, profile_fixture):
        expected_content = profile_fixture.user.username

        assert str(profile_fixture) == expected_content


@pytest.mark.django_db
class TestProfilesIntegration:
    def test_two_profiles_creation_url_and_navigation(self,
                                                      client,
                                                      profile_fixture,
                                                      profile_fixture2):
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
