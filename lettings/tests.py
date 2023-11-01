import pytest

from django.urls import reverse, resolve
from django.test import Client
from lettings.models import Address, Letting
from pytest_django.asserts import assertTemplateUsed


@pytest.fixture
def address_fixture():
    """Fixture to create an Address object."""
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
def address_fixture2():
    """Fixture to create another Address object."""
    number = 55
    street = "av des Champs-Elysées"
    city = "Paris"
    state = "FR"
    zip_code = 75008
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
    """Fixture to create a Letting object."""
    title = "Best villa in town"
    address = address_fixture

    letting = Letting.objects.create(title=title,
                                     address=address)

    return letting


@pytest.fixture
def letting_fixture2(address_fixture2):
    """Fixture to create another Letting object."""
    title = "Flat with jacuzzi"
    address = address_fixture2

    letting = Letting.objects.create(title=title,
                                     address=address)

    return letting


@pytest.fixture
def client():
    """Fixture to create a test client."""
    client = Client()

    return client


@pytest.mark.django_db
class TestLettingsUrls:
    def test_lettings_index_url(self):
        """
        GIVEN a URL path for lettings index is expected,
        WHEN the URL path is retrieved and the view name is resolved,
        THEN it should match the expected path and view name.
        """
        path = reverse("lettings:lettings_index")

        assert path == "/lettings/"
        assert resolve(path).view_name == "lettings:lettings_index"

    def test_letting_url(self, letting_fixture):
        """
        GIVEN a URL path for a specific letting is expected,
        WHEN the URL path is retrieved and the view name is resolved,
        THEN it should match the expected path and view name.
        """
        path = reverse("lettings:letting", kwargs={"letting_id": 1})

        assert path == "/lettings/1/"
        assert resolve(path).view_name == "lettings:letting"


@pytest.mark.django_db
class TestLettingsViews:
    def test_lettings_index_view(self, client, letting_fixture):
        """
        GIVEN a client and a letting object for the lettings index view,
        WHEN the view is accessed,
        THEN it should render with the expected content and status code.
        """
        path = reverse("lettings:lettings_index")
        response = client.get(path)
        content = response.content.decode()

        expected_content = "Best villa in town"

        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/index.html")

    def test_letting_view(self, client, letting_fixture):
        """
        GIVEN a client and a letting object for a specific letting view,
        WHEN the view is accessed,
        THEN it should render with the expected content and status code.
        """
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
        """
        GIVEN an Address object,
        WHEN its string representation is called,
        THEN it should match the Address' number and street.
        """
        expected_content = f'{address_fixture.number} {address_fixture.street}'

        assert str(address_fixture) == expected_content

    def test_letting_model(self, letting_fixture):
        """
        GIVEN a Letting object,
        WHEN its string representation is called,
        THEN it should match the Letting's title.
        """

        expected_content = letting_fixture.title

        assert str(letting_fixture) == expected_content


@pytest.mark.django_db
class TestLettingsIntegration:
    def test_two_lettings_creation_url_and_navigation(self,
                                                      client,
                                                      letting_fixture,
                                                      letting_fixture2):
        """
        GIVEN two lettings are created and navigation between them is expected,
        WHEN the lettings index page and specific letting pages are accessed,
        THEN the content, status codes, and templates used should be as expected.
        """
        path = reverse("lettings:lettings_index")
        response = client.get(path)
        content = response.content.decode()

        expected_content = letting_fixture.title
        expected_content2 = letting_fixture2.title

        assert expected_content in content
        assert expected_content2 in content
        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/index.html")

        path = reverse("lettings:letting", kwargs={"letting_id": 1})
        response = client.get(path)
        content = response.content.decode()

        expected_content = letting_fixture.address.street

        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/letting.html")

        path = reverse("lettings:letting", kwargs={"letting_id": 2})
        response = client.get(path)
        content = response.content.decode()

        expected_content = letting_fixture2.address.street

        assert expected_content in content
        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/letting.html")
