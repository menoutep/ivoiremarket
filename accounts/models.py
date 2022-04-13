from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User(User):
    ROLES = (
        ('SELLER', 'SELLER'),
        ('USER', 'USER'),
        )
    contact = models.PositiveBigIntegerField(null=True, blank=True)
    role = models.CharField(max_length=7, choices=ROLES)
    
    def __str__(self):
        return self.username
    