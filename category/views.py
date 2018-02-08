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

def getQuestionsForQuiz(test_id):
    try:
        questions = Question.objects.all().filter(test=test_id).order_by('?')[:10]
    except Question.DoesNotExist:
        raise Http404('Questions do not exist')
    return questions

def getAnswersForQuestion(question_id):
    try:
        answers = Answer.objects.all().filter(question=question_id)
    except Answer.DoesNotExist:
        raise Http404('Answers do not exist')
    return answers

def quiz(request, test_id):
   quiz = list()
   questions = getQuestionsForQuiz(test_id)
   if questions and len(questions) == 10:
       for question in questions:
           answers = getAnswersForQuestion(question.id)
           if answers and len(answers) > 1:
               quiz.append({question.description: answers})
   return render (request, 'category/quiz.html', {'quiz': quiz, 'test_id': test_id})

def appraisal(request):
    correctness = 0
    count = int(request.POST['count'])
    test = Test.objects.values('title').filter(pk=request.POST['test_id'])
    for i in range(1, count+1):
        i = str(i)
        if Answer.objects.values('correctness').filter(pk=request.POST[i], correctness = True):
            correctness += 1
    score = round(correctness/count * 100, 2)
    return render (request, 'category/appraisal.html', {'score': score, 'test': test})
