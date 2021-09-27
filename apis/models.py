from django.db import models

from django.contrib.auth.models import User



class Post(models.Model):

    post = models.TextField()

    date_create = models.DateTimeField()

    def __str__(self):
        return "{}".format(self.post[:10])