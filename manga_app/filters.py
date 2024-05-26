import django_filters
from manga_app import models


class Manga(django_filters.FilterSet):
    STATUS_CHOICES = (
        ('ongoing', 'Продолжается'),
        ('completed', 'Завершен'),
    )

    title = django_filters.CharFilter(label='Название', lookup_expr='icontains')
    authors = django_filters.CharFilter(label='Автор', lookup_expr='icontains')
    artists = django_filters.CharFilter(label='Художник', lookup_expr='icontains')

    status_title = django_filters.ChoiceFilter(choices=STATUS_CHOICES, label='Статус тайтла')
    status_translation = django_filters.ChoiceFilter(choices=STATUS_CHOICES, label='Статус перевода')

    uploaded_chapters__gt = django_filters.NumberFilter(field_name='uploaded_chapters', lookup_expr='gt', label='Кол-во глав от')
    uploaded_chapters__lt = django_filters.NumberFilter(field_name='uploaded_chapters', lookup_expr='lte', label='Кол-во глав до')
    class Meta:
        model = models.Manga
        exclude = ('photo', 'description', 'release_year', 'status_title', 'status_translation', 'uploaded_chapters', )