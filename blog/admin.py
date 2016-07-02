from django.contrib import admin
from .models import Post #regole python
"""
Il punto significa che il file è contenuto in django (es: .models)
"""
admin.site.register(Post)
