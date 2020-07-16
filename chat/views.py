from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from chat.models import UserInfo
from chat.models import Room
from chat.models import Message
from chat.models import UserRoom

from chat.serializers import UserInfoSerializer
from chat.serializers import RoomSerializer
from chat.serializers import MessageSerializer
from chat.serializers import UserRoomSerializer

def index(request):
    return render(request, 'chat/index.html')

@csrf_exempt
def user_create(request, format=None):
    serializer = UserInfoSerializer(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def user_lookup(request, format=None):
    try:
        userinfo = UserInfo.objects.get(id=request.POST['id'])
    except UserInfo.DoesNotExist:
        return HttpResponse(status=404)

    serializer = UserInfoSerializer(userinfo)
    return JsonResponse(serializer.data)

@csrf_exempt
def user_delete(reqeust):
    try:
        userinfo = UserInfo.objects.get(id=reqeust.POST['id'])
    except UserInfo.DoesNotExist:
        return HttpResponse(status=404)

    if userinfo.delete():
        return HttpResponse('deleted')
    return HttpResponse('delete failed')

@csrf_exempt
def user_update(request):
    org_userinfo = UserInfo.objects.get(id=request.POST['id'])
    serializer = UserInfoSerializer(org_userinfo, data=request.POST)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def room_create(request):
    serializer = RoomSerializer(data=request.POST)
    if serializer.is_valid():
        room_id=Room.objects.get(id=serializer.data['id'])
        user_room = {'user_id': request.POST['user_id'],'room_id': request.POST['room_id'], 'dis_host': True}
        ur_serializer=UserRoomSerializer(data=user_room)
        serializer.save()
        ur_serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def room_join(request):
    return 0

def room_leave(request):
    return 0

def room_destroy(request):
    return 0

def msg_send(reqeust):
    return 0

def msg_read(reqeust):
    return 0

def room_info():
    return 0

