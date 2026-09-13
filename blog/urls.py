from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article-list'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('new/', views.ArticleCreateView.as_view(), name='article-create'),
    path('<int:pk>/update/', views.ArticleUpdateView.as_view(), name='article-update'),
    path('<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article-delete'),
    path('tags/new/', views.TagCreateView.as_view(), name='tag-create'),
    path('categories/new/', views.CategoryCreateView.as_view(), name='category-create'),
    path('api/articles/', views.ArticleListAPI.as_view(), name='article-list-api'),
    path('api/articles/<int:pk>', views.ArticleDetailAPI.as_view(), name='article-detail-api'),
]
