from django.db import models
from django.conf import settings

# Create your models here.

class Note(models.Model):
    author = models.ForeignKey(
      settings.AUTH_USER_MODEL,  
      on_delete=models.CASCADE
    )
    title = models.CharField(max_length=50)
    body = models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
   
    
    def __str__(self):
        return self.title