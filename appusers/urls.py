from django.urls import path, include
from .views import *
app_name="appusers"



urlpatterns = [
    
    path('',index,name='index' ),
    path('course',course,name='course' ),
    path('freeclass',freeclass,name='freeclass' ),
    path('freecourse<int:id>',freecourse,name='freecourse' ),
    path('advanceclass',advanceclass,name='advanceclass' ),
    path('advancecourse<int:id>',advancecourse,name='advancecourse' ),
    path('signup', signup, name='signup'),
    path('login', user_login, name='login'),
    path('dashboard', dashboard, name='dashboard'),
    path('contact', contact, name='contact'),
]