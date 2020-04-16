from django.urls import path
from upload_video import views

urlpatterns = [
    path('', views.upload_video, name='upload_video'),
]