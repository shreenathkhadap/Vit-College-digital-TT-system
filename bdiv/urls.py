from django.contrib import admin
from django.urls import path
from  bdiv import views
urlpatterns = [
     path("",views.index,name= 'index'),
     path("contact",views.contact,name= 'contact'),
     path("tp",views.tp,name= 'tp'),
     path("notes",views.notes,name= 'notes'),
     path("chats",views.chats,name= 'chats')
     
]