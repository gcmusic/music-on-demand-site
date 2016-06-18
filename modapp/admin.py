from django.contrib import admin

from .models import Category, Artist

for model in [Category, Artist]:
    admin.site.register(model)
