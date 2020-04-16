from django.urls import path
from upload_image import views

urlpatterns = [
    path('', views.upload_image, name='upload_image'),
]