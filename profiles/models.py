from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    User profile model.

    This model extends the built-in User model with additional user-specific data.

    Attributes:
        user (User): A one-to-one relationship to the User model.
        favorite_city (str, optional): The user's favorite city (max length: 64).
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
