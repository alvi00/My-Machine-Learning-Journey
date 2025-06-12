from django.db import models
# Create your models here.

class post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title