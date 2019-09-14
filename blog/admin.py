#from django.contrib import admin

# Register your models here.

#Publishing web to admin page(local)
from django.contrib import admin
from .models import Post

admin.site.register(Post)
