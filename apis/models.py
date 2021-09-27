from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField


class UserFields(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    email = EmailField(blank=False)

    avatar = models.ImageField()

    def __str__(self):
        return "{}".format(self.user.username)    

class Post(models.Model):

    post = models.TextField()

    date_create = models.DateTimeField()

    def __str__(self):
        return "{}".format(self.post[:10])