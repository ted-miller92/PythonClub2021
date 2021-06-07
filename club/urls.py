from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resources/', views.resources, name='resources'),
    path('meetings/', views.meetings, name='meetings'),
    path('meetingDetail/<int:id>', views.meetingDetail, name='detail'),
    path('newmeeting/', views.newMeeting, name='newmeeting'),
    path('newmeetingminutes/', views.newMeetingMinutes, name='newmeetingminutes'),
    path('newresource/', views.newResource, name='newresource'),
    path('newevent/', views.newEvent, name='newevent'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]