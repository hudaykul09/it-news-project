from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/edit', ArticleUpdateView.as_view(), name='article_edit'),
    path('filter/<str:catName>/', views.getPostsByTag, name='article_filter'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('comment/<int:pk>/', views.AddComment.as_view(), name='add_comment'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),

]