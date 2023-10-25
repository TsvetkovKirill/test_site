from django.shortcuts import render, redirect, get_object_or_404

from .models import Quiz


def main_page(request):
    context = {'quizzes': Quiz.published.all()}
    return render(request, 'main_test/main_test.html', context)


def home(request):
    return redirect('main_page', permanent=True)


def show_quiz(request, quiz_slug):
    quiz = get_object_or_404(Quiz, slug=quiz_slug)
    context = {'quiz': quiz}
    return render(request, 'main_test/quiz_page.html', context)


def show_quiz_content(request, quiz_slug):
    quiz = get_object_or_404(Quiz, slug=quiz_slug)
    context = {'quiz': quiz}
    return render(request, 'main_test/quiz_content.html', context)
