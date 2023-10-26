from django.contrib import admin
from .models import Quiz, Question, Answer, Tag, UserQuizInteraction, Comment, \
    UserCommentInteraction

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


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(UserQuizInteraction)  # For debugging
class UserInteractionAdmin(admin.ModelAdmin):
    pass


@admin.register(UserCommentInteraction)  # For debugging
class CommentInteractionAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
