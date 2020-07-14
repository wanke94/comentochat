#chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('userlist',views.user_list),
    path('userinfo/<int:id>', views.user_detail)
]