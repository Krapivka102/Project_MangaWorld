from django import forms
from .models import Manga, Chapter, Comment, Genre, Author, Artist


class AddChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['manga', 'name', 'pages_count', 'file']

    def __init__(self, *args, **kwargs):
        super(AddChapterForm, self).__init__(*args, **kwargs)
        self.fields['manga'].queryset = Manga.objects.all()


class MangaForm(forms.ModelForm):
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )
    artists = forms.ModelMultipleChoiceField(
        queryset=Artist.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    class Meta:
        model = Manga
        fields = ['title', 'description', 'photo', 'release_year', 'genres', 'status_title', 'status_translation', 'authors', 'artists']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']