from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout

from .forms import SignUpForm


# Create your views here.
@login_required(login_url='accounts:login', redirect_field_name='')
def index(request):
    context = {
        'username': request.user.username,
        'email': request.user.email,
    }
    return render(request, 'accounts/index.html', context)


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')
    if request.method == 'POST':
        form = SignUpForm(data=request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('Tasks:index')
        else:
            form.add_error(None, 'Invalid username or password')
            return redirect('accounts:signup')
    else:
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username, password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Tasks:index')
            else:
                form.add_error(None, 'Invalid username or password')
                return redirect('accounts:login')
        else:
            print('not valid', form.errors)
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required(login_url='accounts:login', redirect_field_name='')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('Tasks:about-page')
    else:
        return render(request, 'accounts/logout.html', {})
