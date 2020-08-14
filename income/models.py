from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Income(models.Model):
    SOURCE_OPTION = [
        ('SALARY', 'salary'),
        ('BUSINESS', 'business'),
        ('SIDE-HUSTLE', 'side-hustle'),
        ('OTHERS', 'others'),

    ]

    source = models.CharField(choices=SOURCE_OPTION, max_length=255)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.owner) + "'s income"
