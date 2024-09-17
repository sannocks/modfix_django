from django.contrib.auth.models import User
from django.db import models

class Plan(models.Model):
    """
    Represents different plans available for clients.
    Each plan includes a name, description, and the amount of development time included.
    """
    name = models.CharField(max_length=255)
    monthly_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class ClientProfile(models.Model):
    """
    ClientProfile extends the default User model with plan information and available hours.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True, blank=True)
    available_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username}'s profile"
