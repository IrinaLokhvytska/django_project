from django.shortcuts import render
from django.contrib import auth, sessions
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from . models import Category, Test, Question, Answer, UserTestsScore

def index(request):
    if not request.user.is_authenticated:
        return render (request, 'category/authenticate.html', {'user': False})
    else:
        categories = Category.objects.all()
        return render (request, 'category/content.html', {'categories': categories, 'user': request.user})

def authenticate(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
    return HttpResponseRedirect("/")

def registration(request):
    username = request.POST['registration_login']
    password = request.POST['registration_password']
    user = User.objects.create_user(username=username,password=password)
    user.save()
    authenticate = auth.authenticate(username=username, password=password)
    auth.login(request, authenticate)
    return HttpResponseRedirect("/")

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def detail(request, category_id):
    if not request.user.is_authenticated:
        return render (request, 'category/authenticate.html', {'user': False})
    else:
        try:
            category = Category.objects.get(pk=category_id)
            tests = Test.objects.all().filter(category=category_id)
        except Category.DoesNotExist:
            raise Http404('Category does not exist')
        return render (request, 'category/detail.html', {'category': category, 'tests': tests})

def getQuestionsForQuiz(request, test_id):
    try:
        questions = Question.objects.all().filter(test=test_id).order_by('?')[:10]
    except Question.DoesNotExist:
        raise Http404('Questions do not exist')
    quiz = list()
    if questions and len(questions) == 10:
        for question in questions:
            answers = getAnswersForQuestion(question.id)
            if answers and len(answers) > 1:
                quiz.append({question.description: answers})
    return quiz

def getAnswersForQuestion(question_id):
    try:
        answers = Answer.objects.all().filter(question=question_id)
    except Answer.DoesNotExist:
        raise Http404('Answers do not exist')
    return answers

def quiz(request, test_id):
    if not request.user.is_authenticated:
        return render (request, 'category/authenticate.html', {'user': False})
    else:
        quiz =  getQuestionsForQuiz(request, test_id)
        return render (request, 'category/quiz.html', {'quiz': quiz, 'test_id': test_id})

def appraisal(request):
    correctness = 0
    correct_answers = list()
    wrong_answers = list()
    count = int(request.POST['count'])
    user = request.user
    test = Test.objects.values('title').filter(pk=request.POST['test_id'])
    for i in range(1, count+1):
        i = str(i)
        if Answer.objects.values('correctness').filter(pk=request.POST[i], correctness = True):
           correct_answers.append(request.POST[i])
           correctness += 1
        else:
           wrong_answers.append(request.POST[i])
    score = round(correctness/count * 100, 2)
    saveScore(request.POST['test_id'], user, score)
    request.session['correct_answers'] = correct_answers
    request.session['wrong_answers'] = wrong_answers
    return render (request, 'category/appraisal.html', {'score': score, 'test': test})

def getResults(request):
    result = list()
    correct_answers = request.session['correct_answers']
    wrong_answers = request.session['wrong_answers']
    for i in correct_answers:
        questions = Answer.objects.values('question').filter(pk=i)
        for value in questions:
            question = Question.objects.get(pk=value['question'])
            answers = Answer.objects.all().filter(question=value['question'])
            result.append({(question.description, True): answers})
    for i in wrong_answers:
        questions = Answer.objects.values('question').filter(pk=i)
        for value in questions:
            question = Question.objects.get(pk=value['question'])
            answers = Answer.objects.all().filter(question=value['question'])
            result.append({(question.description, False): answers})
    paginator = Paginator(result, 1)
    page = request.GET.get('page')
    result =  paginator.get_page(page)
    return render (request, 'category/answers.html', {'result': result})

def saveScore(test_id, user, estimate):
    estimation = {2: [0, 61], 3: [61, 74], 4: [74, 90], 5: [90, 100]}
    for key, value in estimation.items():
        if estimate in range (value[0], value[1]):
            score = key
    test = Test.objects.get(pk=test_id)
    title = test.title
    score = UserTestsScore(title=title, user=user, test=test, score=score, points=estimate)
    score.save()

def userTestsScore(request):
    if not request.user.is_authenticated:
        return render (request, 'category/authenticate.html', {'user': False})
    else:
        user = request.user.id
        results = UserTestsScore.objects.all().filter(user=user)
        return render (request, 'category/results.html', {'results': results,})