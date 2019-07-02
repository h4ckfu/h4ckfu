from django.db import models

# Create your models here.

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    jobdate = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]