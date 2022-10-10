from django.contrib import admin
from .models import *
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(FeedBack)