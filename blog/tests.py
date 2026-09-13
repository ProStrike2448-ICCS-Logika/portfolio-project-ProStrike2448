from django.test import TestCase

from .models import Article, Category, Tag


class ArticleListTest(TestCase):
    def test_article_list_access(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_article_list_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_article_list_ajax(self):
        response = self.client.get('/', HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/article_list.html')


class ArticleModelTest(TestCase):
    def setUp(self):
        self.category = Category(name='test_category')
        self.category.save()
        self.tag = Tag(name='test_tag')
        self.tag.save()
        return super().setUp()

    def test_article_create(self):
        article = Article.objects.create(title='Test title', content='Test content')
        article.save()
        article.categories.add(self.category)
        article.tags.add(self.tag)

        self.assertEqual(article.title, 'Test title')
        self.assertEqual(article.content, 'Test content')
        self.assertEqual(article.categories.get(pk=self.category.pk), self.category)
        self.assertEqual(article.tags.get(pk=self.tag.pk), self.tag)
        self.assertEqual(article.status, 'draft')

    def test_str(self):
        article = Article.objects.create(title='Test title', content='Test content')
        article.save()
        article.categories.add(self.category)
        article.tags.add(self.tag)

        self.assertEqual(str(article), 'Test title')
