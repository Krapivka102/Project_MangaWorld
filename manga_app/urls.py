from django.urls import path, include
from manga_app import views


urlpatterns = [
    path('', views.index, name='home'),
]