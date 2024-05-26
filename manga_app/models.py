from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Художник'
        verbose_name_plural = 'Художники'

    def __str__(self):
        return self.name


class Manga(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='manga_images/')
    release_year = models.IntegerField()
    genres = models.ManyToManyField(Genre, related_name='mangas')
    status_title = models.CharField(max_length=50)
    status_translation = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author, related_name='mangas')
    artists = models.ManyToManyField(Artist, related_name='mangas')
    uploaded_chapters = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Манга'
        verbose_name_plural = 'Манги'

    def __str__(self):
        return self.title


class Chapter(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='chapters')
    pages_count = models.IntegerField()
    file = models.FileField(upload_to='chapters/')

    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'

    def __str__(self):
        return self.manga.title
