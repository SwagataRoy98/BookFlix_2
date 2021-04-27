from django.db import models

# Create your models here.


class Book(models.Model):
    ol_id = models.CharField(max_length=15, primary_key=True, blank=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='media/cover_pics/')
    desc = models.TextField(blank=True)
    volume = models.IntegerField(blank=False)

    def __str__(self):
        return self.title
