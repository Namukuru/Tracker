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
    path('expenseDetail/<int:pk>',
         views.expense_detail, name='expenseDetail'),
    path('incomeDetail/<int:pk>',
         views.income_detail, name='incomeDetail'),
    path('delete_expenseDetail/<int:pk>',
         views.delete_expenseDetail, name='delete_expenseDetail'),
    path('delete_incomeDetail/<int:pk>',
         views.delete_incomeDetail, name='delete_incomeDetail'),
]
