from django.contrib import admin

from .models import Category, Subcategory, Artist, Rating, Review

for model in [Category, Subcategory, Artist, Rating, Review]:
    admin.site.register(model)
