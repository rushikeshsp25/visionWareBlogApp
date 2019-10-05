from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=150)
    content  =  models.TextField()
    timestamp  = models.DateTimeField(default = timezone.now)
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title+" by "+str(self.posted_by)

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email  =  models.EmailField()
    message  =  models.TextField()
    timestamp  = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.name