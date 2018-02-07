from django.shortcuts import render
from django.http import Http404

from . models import Category, Test, Question, Answer

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

def quiz(request, test_id):
   quiz = {}
   try:
       questions = Question.objects.all().filter(test=test_id)
   except Question.DoesNotExist:
       raise Http404('Questions do not exist')
   for question in questions:
       try:
           answers = Answer.objects.all().filter(question=question.id)
       except Answer.DoesNotExist:
           raise Http404('Answers do not exist')
       quiz[question.description] = answers
   return render (request, 'category/quiz.html', {'quiz': quiz})
