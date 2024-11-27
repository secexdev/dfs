from django.db import models
from django.contrib.auth.models import User
from .utils import get_domain_category  # If this is used elsewhere

# Blocklist Model
class Blocklist(models.Model):
    domain = models.CharField(max_length=255)
    category = models.CharField(max_length=100, choices=[('Adult', 'Adult'), ('Violence', 'Violence'), ('General', 'General')])
    blocked = models.BooleanField(default=True)

    def __str__(self):
        return self.domain

# DNS Logs Model
class DNSLog(models.Model):
    domain = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    action_taken = models.CharField(max_length=10, choices=[('Blocked', 'Blocked'), ('Allowed', 'Allowed')])
    user = models.ForeignKey(User, related_name='logs', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.domain} - {self.action_taken}"
