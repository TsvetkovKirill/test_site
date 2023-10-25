from django.contrib import admin
from .models import Quiz, Question, Answer

from nested_admin.nested import NestedStackedInline, NestedModelAdmin


class AnswerInline(NestedStackedInline):
    model = Answer
    extra = 1


class QuestionInline(NestedStackedInline):
    model = Question
    inlines = [AnswerInline]
    extra = 1


@admin.register(Quiz)
class QuizAdmin(NestedModelAdmin):
    inlines = [QuestionInline]
