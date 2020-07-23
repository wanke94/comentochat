from rest_framework import serializers
from chat.models import UserInfo, Room, Message

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'nick_name', 'url', 'lang']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'host','room_name', 'password', 'guest']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id','user_id','room_id', 'msg','timestamp']

