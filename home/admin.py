# admin.py

from django.contrib import admin
from .models import Article, Comment,Category,Language,Status,Country

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'category', 'language', 'status')
    list_filter = ('status', 'published_date', 'language', 'category')
    search_fields = ('title', 'content', 'author__username')  

admin.site.register(Category)
admin.site.register(Language)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Status)
admin.site.register(Country)