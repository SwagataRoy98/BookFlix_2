import datetime
from allauth.socialaccount.models import SocialAccount
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


class User(models.Model):
    user_name = models.ForeignKey(SocialAccount, related_name='auth_name', on_delete=models.CASCADE)
    current_book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, related_name='user')

