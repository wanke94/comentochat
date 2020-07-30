from django.contrib import admin
from chat.models import UserInfo, Message, Room

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Room)
admin.site.register(Message)