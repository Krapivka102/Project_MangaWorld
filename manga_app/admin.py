from django.contrib import admin
from manga_app import models

admin.site.register(models.Manga)
admin.site.register(models.Genre)
admin.site.register(models.Artist)
admin.site.register(models.Author)
admin.site.register(models.Chapter)

# Register your models here.
