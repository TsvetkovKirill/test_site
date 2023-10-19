from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound


def main_page(request):
    return render(request, 'main_test/main_test.html')


def home(request):
    return redirect('main_page', permanent=True)
