from django.contrib import admin

from .models import Category, Artist, Rating

for model in [Category, Artist, Rating]:
    admin.site.register(model)
