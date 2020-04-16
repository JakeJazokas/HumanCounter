from django.urls import path
from web_interface import views

urlpatterns = [
    path('', views.web_interface, name='web_interface'),
]