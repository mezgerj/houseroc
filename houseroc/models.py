from django.conf import settings
from django.db import models


class BlogPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=512)
    body = models.TextField()
    footer = models.TextField()
    hidden = models.BooleanField(default=False)
    category = models.CharField(max_length=512)
