from django.db import models
from django.urls import reverse
# Create your models here.

class post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail",args=[str(self.id)])