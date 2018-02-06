from django.contrib import admin

from . models import Category, Test, Question, Answer

admin.site.register(Category)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)
