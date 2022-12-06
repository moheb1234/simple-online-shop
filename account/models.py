from django.db import models
from django.contrib.auth.models import User

User._meta.get_field('email')._unique = True


class UserVerify(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.PositiveIntegerField(default=0)
