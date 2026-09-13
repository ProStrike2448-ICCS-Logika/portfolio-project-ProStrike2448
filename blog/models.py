from django.db import models
from django.urls import reverse_lazy


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=256)
    banner = models.ImageField(upload_to='articles/', null=True, blank=True)
    content = models.TextField()
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('blog:article-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_date']
