from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import *
from .forms import TransactionForm, CreateUserForm
from .filters import TransactionFilter


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'Espoire/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'Espoire/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    transactions = Transaction.objects.all()

    total_transactions = transactions.count()

    context = {'transactions': transactions,
               'total_transactions': total_transactions,
               }

    return render(request, 'Espoire/dashboard.html', context)


@login_required(login_url='login')
def allTransactions(request):
    transactions = Transaction.objects.all()

    return render(request, 'Espoire/transactions.html', {'transactions': transactions})


@login_required(login_url='login')
def newform(request):
    submitted = False
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/newform?submitted=True')
    else:
        form = TransactionForm
        if 'submitted' in request.GET:
            submitted=True

    return render(request, 'Espoire/transaction_form.html', {'form':form, 'submitted':submitted})

