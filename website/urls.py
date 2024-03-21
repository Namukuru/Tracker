from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='loginUser'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('expense/', views.add_expense, name='expense'),
    path('income/', views.add_income, name='income'),
    path('UserProfile/', views.user_profile, name='userProfile'),
]
