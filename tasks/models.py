from django.db import models
from django.contrib.auth.models import User
from websites.models import ContentBlock
from clients.models import ClientProfile

class Task(models.Model):
    """
    Represents a task for staff to review and complete edits to content blocks.
    """
    content_block = models.ForeignKey(ContentBlock, on_delete=models.CASCADE)
    staff_member = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    client = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ], default='pending')
    urgency = models.CharField(max_length=20, choices=[
        ('normal', 'Normal'),
        ('urgent', 'Urgent')
    ], default='normal')
    time_spent = models.DurationField(default=0)  # Store time spent on task
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Task for {self.client.user.username}: {self.content_block.block_type}"
