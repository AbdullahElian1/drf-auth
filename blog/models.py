from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

class Blog(models.Model):
    Name = models.CharField(max_length=32)
    Message = models.TextField()
    description = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.Name
