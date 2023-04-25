from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Kategoriýa"

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField('Gysgaça', max_length=200, blank=True)
    body = RichTextField()
    category = models.ManyToManyField(Category, verbose_name='Kategoriyasy', related_name='blog_category')
    photo = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Makala"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=1000)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    parent = models.ForeignKey('self', verbose_name='esasy', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Teswir"

    def __str__(self):
        return self.text
    def get_absolute_url(self):
        return reverse('article_list')