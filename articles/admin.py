from django.contrib import admin
from .models import *

# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)