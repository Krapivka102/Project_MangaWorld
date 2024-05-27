from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from . import models, filters
from django.views import View
from .forms import AddChapterForm
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

        return context


class AddChapterView(LoginRequiredMixin, CreateView):
    form_class = AddChapterForm
    template_name = 'manga_app/addChapter.html'
    success_url = reverse_lazy('home')

class UpdateChapter(LoginRequiredMixin, UpdateView):
    model = models.Chapter
    fields = '__all__'
    template_name = 'manga_app/addChapter.html'
    success_url = reverse_lazy('home')



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
