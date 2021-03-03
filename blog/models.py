from django.db import models
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.name)

class Launguage(models.Model):
    launguage = models.CharField(max_length=120)

    def __str__(self):
        return str(self.launguage)

class Post(models.Model):
    POST_STATUS = [
        ('Draft', 'Draft'),
        ('Published', 'Published'),
        ('Private', 'Private'),
    ]

    title = models.CharField(max_length=120)
    date = models.DateField(auto_now_add=True, auto_now=False)
    url = models.CharField(max_length=120, null=True, blank=True)
    category = models.ManyToManyField(Category, default=None)
    content = RichTextField(max_length=12000, null=True, blank=True)
    status = models.CharField(max_length=120, choices=POST_STATUS)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.title)
    

