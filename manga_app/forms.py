from django import forms
from .models import Manga, Chapter


class AddChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['manga', 'name', 'pages_count', 'file']

    def __init__(self, *args, **kwargs):
        super(AddChapterForm, self).__init__(*args, **kwargs)
        self.fields['manga'].queryset = Manga.objects.all()
