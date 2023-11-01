import pytest

from django.urls import reverse, resolve
from django.test import Client
from lettings.models import Address, Letting
from pytest_django.asserts import assertTemplateUsed


@pytest.fixture
def address_fixture():
    number = 3
    street = "rue des Castors"
    city = "Paris"
    state = "FR"
    zip_code = 75000
    country_iso_code = "FR"

    address = Address.objects.create(number=number,
                                     street=street,
                                     city=city,
                                     state=state,
                                     zip_code=zip_code,
                                     country_iso_code=country_iso_code)

    return address


@pytest.fixture
def letting_fixture(address_fixture):
    title = "Best villa in town"
    address = address_fixture

    letting = Letting.objects.create(title=title,
                                     address=address)

    return letting


@pytest.fixture
def client():
    client = Client()

    return client


@pytest.mark.django_db
class TestLettingsUrls:
    def test_lettings_index_url(self):
        path = reverse("lettings:lettings_index")

        assert path == "/lettings/"
        assert resolve(path).view_name == "lettings:lettings_index"

    def test_letting_url(self, letting_fixture):
        path = reverse("lettings:letting", kwargs={"letting_id": 1})

        assert path == "/lettings/1/"
        assert resolve(path).view_name == "lettings:letting"


@pytest.mark.django_db
class TestLettingsViews:
    def test_lettings_index_view(self, client, letting_fixture):
        path = reverse("lettings:lettings_index")
        response = client.get(path)
        content = response.content.decode()

        expected_content = "Best villa in town"

        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/index.html")

    def test_letting_view(self, client, letting_fixture):
        path = reverse("lettings:letting", kwargs={"letting_id": 1})
        response = client.get(path)
        content = response.content.decode()

        expected_content = "rue des Castors"

        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/letting.html")


@pytest.mark.django_db
class TestLettingsModels:
    def test_address_model(self, address_fixture):
        expected_content = f'{address_fixture.number} {address_fixture.street}'

        assert str(address_fixture) == expected_content

    def test_letting_model(self, letting_fixture):
        expected_content = letting_fixture.title

        assert str(letting_fixture) == expected_content
