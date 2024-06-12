from django.db import models

# Create your models here.
class Create(models.Model):
    title=models.CharField(max_length=50)
    desc=models.TextField()
    

    def __str__(self):
        return self.title