from django.urls import path

from core.views import Home, Profile_List, Profile_Create

app_name = 'core'
urlpatterns = [
    path('',Home.as_view()),
    path('profile/', Profile_List.as_view(), name='profile_list'),
    path('profile/create/', Profile_Create.as_view(), name='profile_create'),
]