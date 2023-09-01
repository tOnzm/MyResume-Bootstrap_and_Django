from django.urls import path
from . import views




urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('projects/',views.projects,name='projects'),
    path('contact/',views.contact,name='contact'),
    path('resume/',views.resume,name='resume'), 

    path('upload/', views.upload_image, name='upload_image'),


   

]

