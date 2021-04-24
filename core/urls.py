#PACKAGE IMPORT
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

#LOCAL IMPORT
from core import views

urlpatterns = [
   path('api/user', views.Login.as_view()),
   path('api/weight_types', views.Weight_typesViews.as_view()),
   path('api/operators', views.OperatorsViews.as_view()),
   path('api/qodex_achive', views.Qodex_achiveViews.as_view()),
]
