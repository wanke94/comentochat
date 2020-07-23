#chat/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('usercreate/',views.user_create, name='usercreate'),
    path('userinfo/',views.user_lookup, name='userinfo'),
    path('userdelete/',views.user_delete, name='userdelete'),
    path('userupdate/',views.user_update, name='userupdate'),
    path('roomcreate/',views.room_create, name='roomcreate'),
    path('roomjoin/',views.room_join, name='roomjoin'),
    path('roomleave/',views.room_leave, name='roomleave'),
    path('roomdestroy/',views.room_destroy, name='roomdestroy'),
    path('msgsend/',views.msg_send, name='msgsend'),
    path('msgread/',views.msg_read, name='msgread'),
    path('roominfo/',views.room_info, name='room_info'),

]

urlpatterns = format_suffix_patterns(urlpatterns)