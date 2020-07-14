from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from chat.serializers import UserInfoSerializer
from rest_framework.response import Response

from chat.models import UserInfo


def index(request):
    return render(request, 'chat/index.html')


@api_view(['GET', 'POST'])
def user_list(request):
#user 전체 리스트

    if request.method == 'GET':
        snippets = UserInfo.objects.all()
        serializer = UserInfoSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, id):
    """
    talend api에서 GET으로 http://127.0.0.1:8000/chat/userinfo?id=1 실행시 404_NOT_FOUND응답을 받습니다.
    urls 설정을   path('userinfo', views.user_detail)로 변경 후 id를 매개변수가 아닌 메소드 내에서 임의로 변수 1로 지정후
    실행하면 제대로된 응답을 받습니다.
    문제점이 무엇인지 알고 싶습니다.
    """

    try:
        user_info = UserInfo.objects.get(id=id)
    except UserInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    #user_lookup
    if request.method == 'GET':
        serializer = UserInfoSerializer(user_info)
        return Response(serializer.data)

    #user_create, user_update
    elif request.method == 'PUT':
        serializer = UserInfoSerializer(user_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #user_delete
    elif request.method == 'DELETE':
        user_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
