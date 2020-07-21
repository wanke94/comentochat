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
    path('room_join/',views.room_join, name='roomjoin'),

]

urlpatterns = format_suffix_patterns(urlpatterns)