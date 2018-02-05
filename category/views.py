from django.shortcuts import render
from django.http import Http404

from . models import Category
from . models import Test

def index(request):
   categories = Category.objects.all()
   return render (request, 'category/content.html', {'categories': categories})

def detail(request, category_id):
   try:
       category = Category.objects.get(pk=category_id)
       tests = Test.objects.all().filter(category=category_id)
   except Category.DoesNotExist:
       raise Http404('Category does not exist')
   return render (request, 'category/detail.html', {'category': category, 'tests': tests})
