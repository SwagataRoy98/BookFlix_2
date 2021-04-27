import datetime

from django.db import models
import uuid
# Create your models here.


class Book(models.Model):
    ol_id = models.CharField(max_length=20, primary_key=True, blank=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='media/cover_pics/')
    desc = models.TextField(blank=True)
    volume = models.IntegerField(blank=False)

    def __str__(self):
        return self.title


class Transactions(models.Model):
    transaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    ol_id = models.CharField(max_length=20, blank=False)
    user_name = models.CharField(max_length=100, blank=True)
    date_time = models.DateTimeField(default=datetime.datetime)

    def __str__(self):
        return f'{ self.user_name } borrowed { self.ol_id } at { self.date_time }'
