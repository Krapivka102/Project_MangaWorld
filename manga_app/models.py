from django.db import models


class Genre(models.Model):
    name = models.CharField('Название жанра', max_length=50)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField('Имя автора', max_length=100)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField('Имя художника', max_length=100)

    class Meta:
        verbose_name = 'Художник'
        verbose_name_plural = 'Художники'

    def __str__(self):
        return self.name


class Manga(models.Model):
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', blank=True)
    photo = models.ImageField(upload_to='manga_images/')
    release_year = models.IntegerField('Год создания')
    genres = models.ManyToManyField(Genre, verbose_name='Жанр')
    status_title = models.CharField('Статус выпуска', max_length=50)
    status_translation = models.CharField('Статус перевода', max_length=50)
    authors = models.ManyToManyField(Author, verbose_name='Автор')
    artists = models.ManyToManyField(Artist, verbose_name='Художник')
    uploaded_chapters = models.IntegerField('Количество глав',default=0)

    class Meta:
        verbose_name = 'Манга'
        verbose_name_plural = 'Манги'

    def __str__(self):
        return self.title


class Chapter(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='chapters')
    pages_count = models.IntegerField('Количество страниц')
    file = models.FileField(upload_to='chapters/')

    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'

    def __str__(self):
        return self.manga.title
