from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='pic')
    desc=models.TextField()

class Meet(models.Model):
    image = models.ImageField(upload_to='pic')
    name = models.CharField(max_length=200)
    desc = models.TextField()
    def __str__(self):
        return self.name