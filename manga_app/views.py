from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models, filters
from django.views import View
from .forms import AddChapterForm, CommentForm, MangaForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.db.models import Count


class MangaList(ListView):
    model = models.Manga
    context_object_name = "mangas"
    template_name = 'manga_app/index.html'
    paginate_by = 3

    def get_filters(self):
        return filters.Manga(self.request.GET)

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        genre = models.Genre.objects.all()
        context["filters"] = self.get_filters()
        context["is_admin"] = self.request.user.groups.filter(name='Администраторы').exists()

        return context


class MangaDetailView(DetailView):
    model = models.Manga
    template_name = 'manga_app/manga_detail.html'
    context_object_name = 'manga'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = models.Comment.objects.filter(manga=self.get_object()).order_by('-created_at')
        context['form'] = CommentForm()
        context["is_admin"] = self.request.user.groups.filter(name='Администраторы').exists()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.manga = self.get_object()
            comment.save()
            return redirect('manga_detail',
                            pk=self.get_object().pk)
        return render(request, self.template_name, {'form': form})

class DownloadChapterView(View):
    def get(self, request, *args, **kwargs):
        chapter_id = kwargs.get('chapter_id')
        chapter = models.Chapter.objects.get(id=chapter_id)
        response = FileResponse(chapter.file.open('rb'))
        response['Content-Disposition'] = f'attachment; filename="{chapter.name}"'
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        chapters = models.Chapter.objects.filter(manga=self.object.id).order_by('-id')
        context['chapters'] = chapters
        return context


class AddMangaView(LoginRequiredMixin, CreateView):
    model = models.Manga
    form_class = MangaForm
    template_name = 'manga_app/add_manga.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='Администраторы').exists():
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_admin'] = self.request.user.groups.filter(name='Администраторы').exists()
        return context



class AddChapterView(LoginRequiredMixin, CreateView):
    form_class = AddChapterForm
    template_name = 'manga_app/addChapter.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='Администраторы').exists():
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_admin'] = self.request.user.groups.filter(name='Администраторы').exists()
        return context


class DeleteChapterView(LoginRequiredMixin, DeleteView):
    model = models.Chapter
    template_name = 'manga_app/delete_chapter.html'
    success_url = reverse_lazy('home')
    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='Администраторы').exists():
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_admin'] = self.request.user.groups.filter(name='Администраторы').exists()
        return context


class UpdateMangaView(LoginRequiredMixin, UpdateView):
    model = models.Manga
    fields = ['title', 'description', 'photo', 'release_year', 'genres', 'status_title', 'status_translation',
              'authors', 'artists']

    template_name = 'manga_app/add_manga.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='Администраторы').exists():
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_admin'] = self.request.user.groups.filter(name='Администраторы').exists()
        return context


class UpdateChapter(LoginRequiredMixin, UpdateView):
    model = models.Chapter
    fields = '__all__'
    template_name = 'manga_app/addChapter.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='Администраторы').exists():
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_admin'] = self.request.user.groups.filter(name='Администраторы').exists()
        return context



# class AddChapterView(View):
#     form_class = AddChapterForm
#     template_name = 'manga_app/addChapter.html'
#     success_url = reverse_lazy('home')
#
#
#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})
#
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect(self.success_url)
#         return render(request, self.template_name, {'form': form})
