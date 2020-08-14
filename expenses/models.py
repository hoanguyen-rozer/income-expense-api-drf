from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Expense(models.Model):
    CATEGORY_OPTION = [
        ('ONLINE_SERVICE', 'service'),
        ('TRAVEL', 'travel'),
        ('FOOD', 'food'),
        ('RENT', 'rent'),
        ('OTHERS', 'others'),

    ]

    category = models.CharField(choices=CATEGORY_OPTION, max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2, max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)
    
    