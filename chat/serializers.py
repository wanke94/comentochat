from rest_framework import serializers
from chat.models import UserInfo

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'nick_name', 'url', 'lang']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['user_id','room_name', 'password']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['user_id','room_id', 'message','timestamp']

class UserRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['user_id','room_id', 'dis_host']
