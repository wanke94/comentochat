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
    user_id = models.ForeignKey(UserInfo, to_field='id', on_delete=models.CASCADE)
    room_name = models.CharField(max_length=200)
    password = models.IntegerField()

    def __str__(self):
        return self.user_id

class Message(models.Model):
    user_id = models.ForeignKey(UserInfo, to_field='id', on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, to_field='id',on_delete=models.CASCADE)
    msg = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id

class UserRoom(models.Model):
    user_id = models.ForeignKey(UserInfo, to_field='id', on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, to_field='id',on_delete=models.CASCADE)
    dis_host = models.BooleanField(default=False)

    class Meta:
        unique_together = (("user_id", "room_id"))

    def __str__(self):
        return self.user_id