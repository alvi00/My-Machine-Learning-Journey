from django.db import models

# Create your models here.

class Post(models.Model):
    tittle=models.CharField(max_length=200)
    content=models.TextField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tittle