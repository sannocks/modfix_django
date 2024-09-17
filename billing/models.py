from django.db import models
from django.contrib.auth.models import User

class Invoice(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('paid', 'Paid')])
