from django.db import models


# Create your models here.
class UserInfo(models.Model):
    nick_name = models.CharField(max_length=100)
    lang = models.CharField(max_length=50, default='kor')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nick_name
