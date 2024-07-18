from django.db import models
from django.utils import timezone
#django.contrib.auth.models imort user would be important since a user can create multiple posts

from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

def __str__(self):
    return self.title


    
