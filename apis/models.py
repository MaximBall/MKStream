from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField


class UserFields(models.Model):

    email = EmailField(blank=False)

    avatar = models.ImageField(blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return "{}".format(self.user)    

class Post(models.Model):

    post = models.TextField()

    date_create = models.DateTimeField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return "{}".format(self.post[:10])