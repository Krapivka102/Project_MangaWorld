from django.urls import path, include
from manga_app import views


urlpatterns = [
    path('', views.MangaList.as_view(), name='home'),
    path('addchapter/', views.AddChapterView.as_view(), name='addchapter'),
    path('addchapter/<int:pk>/', views.UpdateChapter.as_view(), name='updatechapter'),
    path('delete-chapter/<int:pk>/', views.DeleteChapterView.as_view(), name='delete_chapter'),
    path('addmanga/', views.AddMangaView.as_view(), name='addmanga'),
    path('addmanga/<int:pk>/', views.UpdateMangaView.as_view(), name='updatemanga'),
    path('manga_detail/<int:pk>/', views.MangaDetailView.as_view(), name='manga_detail'),
    path('download/chapter/<int:chapter_id>/', views.DownloadChapterView.as_view(), name='download_chapter'),
]