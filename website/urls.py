from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('reports/', views.reports, name='reports'),
    path('budget/', views.budget, name='budget'),
    path('login/', views.login_user, name='loginUser'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('expense/', views.add_expense, name='expense'),
    path('income/', views.add_income, name='income'),
    path('UserProfile/', views.user_profile, name='userProfile'),
    path('expenseDetail/<int:pk>',
         views.expense_detail, name='expenseDetail'),
    path('incomeDetail/<int:pk>',
         views.income_detail, name='incomeDetail'),
    path('delete_expense/<int:pk>',
         views.delete_expense, name='delete_expense'),
    path('delete_income/<int:pk>',
         views.delete_income, name='delete_income'),
    path('update_expense/<int:pk>',
         views.update_expense, name='update_expense'),
    path('update_income/<int:pk>',
         views.update_income, name='update_income'),
]
