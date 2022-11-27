from django.db import models
from django.utils.translation import gettext_lazy as _

class User(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    SEX_CHOICES = (
        ('man', 'Женщина'),
        ('woman', 'Мужчина'),
    )

    sex = models.CharField(max_length=6, choices=SEX_CHOICES, default='woman')

    city = models.CharField(max_length=100)
    old = models.CharField(max_length=100)






