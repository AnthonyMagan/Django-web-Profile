from django.urls import path
from . import views #this imports the blog/views.py

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    #path('hello', views.all_blogs, name='all_blogs'),  #you can now reach this blog by using localhost:8000/blog/hello. This is useful if you have alot of app from a web-application
    #add a new path S5L46. Dynamically updates the int passing the number to details
    path('<int:blog_id>/', views.detail, name='detail'),
]
