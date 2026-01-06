from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Define Roles
    ADMIN = 'admin'
    SALES = 'sales'
    INVENTORY = 'inventory'
    MANAGER = 'manager'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (SALES, 'Sales Clerk'),
        (INVENTORY, 'Inventory Manager'),
        (MANAGER, 'Manager (Viewer)'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=SALES)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"