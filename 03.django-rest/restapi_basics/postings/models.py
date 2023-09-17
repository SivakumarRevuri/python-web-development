from django.db import models
from django.conf import settings

# Create your models here.
class BlogPost(models.Model):
    user = models.CharField(max_length=64, null=True, blank=True)
    title = models.CharField(max_length=120, null=True, blank = True)
    content = models.TextField(max_length=180, null=True, blank= True)    
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.user