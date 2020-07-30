from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.utils import timezone
from rest_framework.parsers import JSONParser

from chat.models import UserInfo
from chat.models import Room
from chat.models import Message

from chat.serializers import UserInfoSerializer
from chat.serializers import RoomSerializer
from chat.serializers import MessageSerializer


def index(request):
    return render(request, 'chat/index.html')


@csrf_exempt
def user_create(request):
    data = JSONParser().parse(request)
    serializer = UserInfoSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def user_lookup(request):
    data = JSONParser().parse(request)
    try:
        userinfo = UserInfo.objects.get(id=data["id"])
    except UserInfo.DoesNotExist:
        context = {
            "code": 404,
            "message": 'User \''+data["id"]+'\' Does Not Exist'
        }
        return JsonResponse(context)

    serializer = UserInfoSerializer(userinfo)
    return JsonResponse(serializer.data)


@csrf_exempt
def user_delete(reqeust):
    data = JSONParser().parse(reqeust)
    try:
        userinfo = UserInfo.objects.get(id=data["id"])
    except UserInfo.DoesNotExist:
        context = {
            "code": 404,
            "message": 'User \'' + data["id"] + '\' Does Not Exist'
        }
        return JsonResponse(context)

    if userinfo.delete():
        return HttpResponse('deleted')
    return HttpResponse('delete failed')


@csrf_exempt
def user_update(request):
    data = JSONParser().parse(request)
    org_user = UserInfo.objects.get(id=data["id"])
    serializer = UserInfoSerializer(org_user, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def room_create(request):
    data = JSONParser().parse(request)
    serializer = RoomSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def room_join(request):
    data = JSONParser().parse(request)
    guest_id = data['user_id']
    room_id = data['room_id']
    pwd = data['password']

    #room 정보가져오기
    room = Room.objects.get(id=room_id)

    # check password
    if room.password == pwd:
        room.guest.add(guest_id)
        serializer = RoomSerializer(room)
        return JsonResponse(serializer.data)
    return HttpResponse('password incorrect!!')

@csrf_exempt
def room_leave(request):
    data = JSONParser().parse(request)
    guest_id = data['user_id']
    room_id = data['room_id']

    #room에 guest id가 없는 경우
    try:
        room = Room.objects.get(id=room_id, guest=guest_id)
        room.guest.remove(guest_id)
        return HttpResponse('success')
    except Room.DoesNotExist:
        return HttpResponse('User \''+guest_id+'\' Does Not Exist')

@csrf_exempt
def room_destroy(request):
    data = JSONParser().parse(request)
    user_id = data['user_id']
    room_id = data['room_id']

    #room 있는지 확인
    try:
        room = Room.objects.get(id=room_id)
    except Room.DoesNotExist:
        return HttpResponse('This Room Does Not Exist')

    #user_id가 host인지 체크
    if room.host.id != user_id:
        return HttpResponse("Unauthorized")
    elif room.delete():
        return HttpResponse('destroyed')
    return HttpResponse('destroy failed')

@csrf_exempt
def msg_send(reqeust):
    data = JSONParser().parse(reqeust)
    room_id = data['room_id']

    # room이 destroyed 됐을 때
    try:
        room = Room.objects.get(id=room_id)
    except Room.DoesNotExist:
        return HttpResponse('This Room Does Not Exist')

    serializer = MessageSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def msg_read(reqeust):
    data = JSONParser().parse(reqeust)
    time = datetime.strptime(data['timestamp'], '%Y-%m-%d %H:%M:%S')

    room_id = data['room_id']
    msg = Message.objects.all().filter(room_id=room_id).filter(timestamp__gte=time)
    serializer = MessageSerializer(msg, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def room_info(request):
    data = JSONParser().parse(request)
    room_id = data['room_id']
    try:
        room = Room.objects.get(id=room_id)
    except Room.DoesNotExist:
        return HttpResponse(status=404)

    serializer = RoomSerializer(room)
    return JsonResponse(serializer.data)
