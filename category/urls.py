from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('authenticate/', views.authenticate, name='authenticate'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.logout, name='logout'),
    path('<int:category_id>/', views.detail, name='detail'),
    path('<int:test_id>', views.quiz, name='quiz'),
    path('appraisal/', views.appraisal, name='appraisal'),
    path('result/', views.getResults, name='result'),
    path('score/', views.userTestsScore, name='score'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)