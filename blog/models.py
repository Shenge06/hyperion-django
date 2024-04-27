from django.db import models

# Create your models here.
class Post(models.Model):
    # Default behaviour - Django creates primary keys for you
    title = models.CharField(max_length=140)
    body = models.TextField()
    signature = models.CharField(max_length=140, default="nkululeko")
    date = models.DateTimeField()

    def __str__(self):
        return self.title
