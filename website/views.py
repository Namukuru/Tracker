from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, ExpenseForm, IncomeForm
from .models import Expense, Income


def home(request):
    # Check to see if user is logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # User Authentication
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Log in successful!")
            return redirect('login_user')
        else:
            messages.success(request, "An error occurred. Please try again.")
            return redirect('login_user')
    else:
        return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def user_profile(request):
    expenses = request.user.expense_set.all()  # Filter by logged-in user
    incomes = request.user.income_set.all()
    total_expenses = 0
    total_income = 0
    for expense in expenses:
        total_expenses += expense.amount
    for income in incomes:
        total_income += income.amount
    balance = total_income - total_expenses
    context = {
        'expenses': expenses,
        'incomes': incomes,
        'total_expenses': total_expenses,
        'total_income': total_income,
        'balance': balance
    }

    return render(request, 'userProfile.html', context)


def login_user(request):
    # Check to see if user is logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # User Authentication
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Log in successful!")
            return redirect('loginUser')
        else:
            messages.success(request, "An error occurred. Please try again.")
            return redirect('loginUser')
    else:
        return render(request, 'loginUser.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "Log out successful!")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate and log them in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


def add_expense(request):
    form = ExpenseForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_expense = form.save(commit=False)
            new_expense.user = request.user  # Associate the expense with the logged-in user
            new_expense.save()
            messages.success(
                request, "You have successfully added the expense")
        return redirect('home')
    return render(request, 'expense.html', {'form': form})


def add_income(request):
    form = IncomeForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_income = form.save(commit=False)
            new_income.user = request.user  # Associate the income with the logged-in user
            new_income.save()
            messages.success(request, "You have successfully added the income")
        return redirect('userProfile')
    return render(request, 'income.html', {'form': form})


def expense_detail(request, pk):
    expenseDetail = Expense.objects.get(id=pk)
    return render(request, 'expenseDetail.html', {'expenseDetail': expenseDetail})


def income_detail(request, pk):
    incomeDetail = Income.objects.get(id=pk)
    return render(request, 'incomeDetail.html', {'incomeDetail': incomeDetail})


def delete_expense(request, pk):
    delete_expense = Expense.objects.get(id=pk)
    delete_expense.delete()
    messages.success(request, "You have successfully deleted the expense !")
    return redirect('userProfile')


def delete_income(request, pk):
    delete_income = Income.objects.get(id=pk)
    delete_income.delete()
    messages.success(request, "You have successfully deleted the income !")
    return redirect('userProfile')
