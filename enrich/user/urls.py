from django.urls import path
from .api import views

urlpatterns=[
    path('checkserver',views.test_server,name='checkserver'),
    path('group',views.group,name='group'),
    path('user',views.user,name='user'),
    path('languageconvert',views.languageconvert,name='lan_convert')
]