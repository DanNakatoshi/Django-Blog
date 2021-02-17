from django.db import models
from datetime import datetime, date
# from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return str(self.name)

class Post(models.Model):
    title = models.CharField(max_length=120)
    date = models.DateField(auto_now_add=True, auto_now=False)
    yt_url = models.CharField(max_length=120, null=True, blank=True)
    yt_eng = models.CharField(max_length=120, null=True, blank=True)
    github = models.CharField(max_length=120, null=True, blank=True)
    # category = models.ForeignKey(Category,  on_delete=models.DO_NOTHING)
    content = RichTextField(max_length=12000, null=True, blank=True)
    # content = RichTextUploadingField(blank=True, null=True)
    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-date']
    
