from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import generics

from . import forms, models, serializers


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = forms.TagCreationForm
    template_name = 'blog/tag_create_form.html'
    success_url = reverse_lazy('blog:article-create')


class CategoryCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = forms.CategoryCreationForm
    template_name = 'blog/category_create_form.html'
    success_url = reverse_lazy('blog:article-create')


class ArticleListView(generic.ListView):
    model = models.Article
    context_object_name = 'articles'
    template_name = 'blog/index.html'
    paginate_by = 1

    def get(self, request: HttpRequest):
        super().get(request)

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return render(
                request=request,
                template_name='blog/article_list.html',
                context=self.get_context_data(),
            )

        return render(
            request=request, template_name=self.template_name, context=self.get_context_data()
        )


class ArticleDetailView(generic.DetailView):
    model = models.Article
    context_object_name = 'article'
    template_name = 'blog/article_detail.html'


class ArticleCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = forms.ArticleCreationForm
    template_name = 'blog/article_create_form.html'
    success_url = reverse_lazy('blog:article-list')


class ArticleUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.Article
    form_class = forms.ArticleCreationForm
    template_name = 'blog/article_update.html'


class ArticleDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = models.Article
    template_name = 'blog/article_delete.html'
    success_url = reverse_lazy('blog:article-list')


class ArticleListAPI(generics.ListCreateAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer


class ArticleDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
