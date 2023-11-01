from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents a physical address.

    Fields:
        number (PositiveIntegerField): The street number.
        street (CharField): The street name.
        city (CharField): The city.
        state (CharField): The state code (e.g., CA for California).
        zip_code (PositiveIntegerField): The ZIP code.
        country_iso_code (CharField): The ISO country code (e.g., USA for the United States).
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """Returns a string representation of the address in the format "number street"."""
        return f'{self.number} {self.street}'

    class Meta:
        """Plural name for the model in the admin interface."""
        verbose_name_plural = "addresses"


class Letting(models.Model):
    """
    Represents a letting (e.g., a property for rent).

    Fields:
        title (CharField): The title or name of the letting.
        address (OneToOneField): A reference to the address associated with this letting.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """Returns the title of the letting."""
        return self.title
