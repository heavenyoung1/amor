from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    #profileimg = pass
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username




# class User(models.Model):
#     name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#
#     SEX_CHOICES = (
#         ('man', 'Женщина'),
#         ('woman', 'Мужчина'),
#     )
#
#     sex = models.CharField(max_length=6, choices=SEX_CHOICES, default='woman')
#
#     city = models.CharField(max_length=100)
#     old = models.CharField(max_length=100)






