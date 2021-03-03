from django.contrib import admin
from .models import Post, Launguage, Category

admin.site.register(Launguage)
admin.site.register(Category)
admin.site.register(Post)