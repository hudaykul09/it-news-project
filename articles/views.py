from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Article, Category
from .forms import CommentForm 
# Create your views here.

class CategoryFilter:
    def get_category(self):
        return Category.objects.all()

class ArticleListView(CategoryFilter, ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(CategoryFilter, DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'summary', 'body', 'category', 'photo')
    template_name = 'article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Article
    fields = ('title', 'summary', 'body', 'category', 'photo', 'author')
    template_name = 'article_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

class AddComment(View):
    def post(self, request, pk):
        form= CommentForm(request.POST)
        form.instance.author = self.request.user
        article = Article.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.article_id = pk
            form.save()
        return redirect(article.get_absolute_url())


def getPostsByTag(request, catName):
    filter = True
    template_name = 'article_list.html'
    posts = Article.objects.filter(category__name=catName).all()
    context = {"posts":posts, "filter":filter}
    return render(request=request, template_name=template_name, context=context)


