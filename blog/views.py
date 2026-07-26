from django.views import generic

from . import models


class ArticleListView(generic.ListView):
    model = models.Article
    context_object_name = 'articles'
    template_name = 'blog/article_list.html'


class ArticleDetailView(generic.DetailView):
    model = models.Article
    context_object_name = 'article'
    template_name = 'blog/article_detail.html'
