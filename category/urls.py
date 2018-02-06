from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:category_id>/', views.detail, name='detail'),
    path('<int:test_id>', views.quiz, name='quiz'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)