from django.urls import path, include
from manga_app import views


urlpatterns = [
    path('', views.MangaList.as_view(), name='home'),
    path('addchapter/', views.AddChapterView.as_view(), name='addchapter'),
]