from django.contrib import admin

from .models import Category, Subcategory, Artist, Rating

for model in [Category, Subcategory, Artist, Rating]:
    admin.site.register(model)
