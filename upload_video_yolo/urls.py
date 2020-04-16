from django.urls import path
from upload_video_yolo import views

urlpatterns = [
    path('', views.upload_video_yolo, name='upload_video_yolo'),
]