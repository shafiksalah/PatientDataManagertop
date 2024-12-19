from django.urls import path
from . import views

urlpatterns = [
    path('', views.الرئيسية, name='الرئيسية'),
    path('تسجيل-الدخول/', views.تسجيل_الدخول, name='تسجيل-الدخول'),
    path('إضافة-مريض/', views.إضافة_مريض, name='إضافة-مريض'),
    path('إضافة-اشتراك/', views.إضافة_اشتراك, name='إضافة-اشتراك'),
    path('إضافة-دفع/', views.إضافة_دفع, name='إضافة-دفع'),
]
