from django.contrib import admin
# include: allows to include other files into this file
from django.urls import path, include
from todo_list import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_list.urls')),
]
