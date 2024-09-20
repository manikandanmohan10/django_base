from django.contrib import admin
from .models import User, Book, UserProfile, Library
# Register your models here.

admin.site.register(User)
admin.site.register(Book)
admin.site.register(UserProfile)
admin.site.register(Library)
