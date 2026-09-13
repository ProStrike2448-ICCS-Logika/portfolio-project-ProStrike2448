from django import forms

from .models import Article, Category, Tag


class TagCreationForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'


class CategoryCreationForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ArticleCreationForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'banner', 'content', 'categories', 'tags', 'status']
