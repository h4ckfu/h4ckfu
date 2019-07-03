from django.db import models

# Create your models here.
class Cert(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length = 256)
    summary = models.CharField(max_length = 256)