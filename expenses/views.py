import re
from readline import redisplay
from django.shortcuts import render, redirect
from .models import Expense
from .form import ExpensesForm

def home(request):
    data = {}
    data['expenses'] = Expense.objects.all()
    return render(request, "expenses/home/home.html", data)


def form(request):
    data = {}
    form = ExpensesForm(request.POST or None)
    data['form'] = form
    if form.is_valid():
        form.save()
        return redirect('url_home')

    return render(request, "expenses/form/form.html", data)

def update(request, pk):
    data = {}
    expense = Expense.objects.get(pk=pk)
    form = ExpensesForm(request.POST or None, instance=expense)
    data['expense'] = expense
    data['form'] = form
    if form.is_valid():
        form.save()
        return redirect('url_home')

    return render(request, "expenses/form/form.html", data)

def delete(request, pk):
    data = {}
    expense = Expense.objects.get(pk=pk)
    expense.delete()
    return redirect('url_home')