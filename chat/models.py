from typing import re

from django.db import models


# Create your models here.
class UserInfo(models.Model):
    LANGUAGE_CHOICES = (
        ('kor', 'korean'),
        ('eng', 'english'),
        ('chn', 'chinese'),
    )

    id = models.CharField(max_length=100, primary_key=True)
    nick_name = models.CharField(max_length=100)
    url = models.URLField(null=True)
    lang = models.CharField(max_length=3, default='kor', choices=LANGUAGE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nick_name


class Room(models.Model):
    room_name = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    host = models.ForeignKey(UserInfo, related_name='host', on_delete=models.CASCADE)
    guest = models.ManyToManyField(UserInfo, related_name='guest', blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.room_name


class Message(models.Model):
    user_id = models.ForeignKey(UserInfo, related_name='user_id', on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, related_name='room_id', on_delete=models.CASCADE)
    msg = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.user_id)
