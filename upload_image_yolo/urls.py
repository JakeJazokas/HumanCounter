from django.urls import path
from upload_image_yolo import views

urlpatterns = [
    path('', views.upload_image_yolo, name='upload_image_yolo'),
]