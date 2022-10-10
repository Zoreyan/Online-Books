import uuid
from django.db import models
# Create your models here.



class Category(models.Model):
    title = models.CharField(max_length=120)
    framework = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class Book(models.Model):
    LANGUAGES = [
        ('en', 'English'),
        ('ru', 'Russian')
    ]
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=800, null=True)
    image = models.ImageField(upload_to='book_articles/')
    author = models.CharField(max_length=100, null=True)
    category = models.ManyToManyField(Category)
    language = models.CharField(choices=LANGUAGES, default='ru', max_length=22)
    writed = models.CharField(max_length=4, null=True)
    file =  models.FileField(upload_to='pdf_files', default='file.pdf')
    created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.title


class FeedBack(models.Model):
    email = models.EmailField()
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.email +' --- '+ self.text