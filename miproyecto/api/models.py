from __future__ import unicode_literals

from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField(max_length=200)
    def __uniode__(self):
        return self.title
    

# Create your models here.
