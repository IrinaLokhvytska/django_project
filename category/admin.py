from django.contrib import admin

from . models import Category
from . models import Test

admin.site.register(Category)
admin.site.register(Test)
