from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginUserForm, RegisterUserForm
from django.urls import reverse


def login_user(request):
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('main_page'))
    else:
        form = LoginUserForm()
    return render(request, "users/login.html", {"form": form})


def logout_user(request):
    logout(request)
    # return HttpResponseRedirect(reverse("users:login"))
    return render(request, "users/logout.html")
def register_done(request):
    return render(request, "users/register_done.html", {"form": "Вы успешно зарегистрировались!"})
def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'users/register_done.html')
    else:
        form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form})


