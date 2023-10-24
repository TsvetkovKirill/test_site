from django.contrib.auth.models import User
from django.db import models


class Quiz(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0
        PUBLISHED = 1
        DELETED = 2

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'

    title = models.CharField(max_length=100, unique=True,
                             verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Слаг')
    description = models.TextField(max_length=1500, verbose_name='Описание')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                               related_name='quizzes', verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Создано')
    edited_at = models.DateTimeField(auto_now=True,
                                     verbose_name='Изменено')
    status = models.IntegerField(choices=Status.choices, verbose_name='Статус',
                                 default=Status.DRAFT)

    def __str__(self):
        return self.title


class Question(models.Model):
    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE,
                             related_name='questions', verbose_name='Квиз')
    content = models.TextField(max_length=3000, verbose_name='Содержание')


class Answer(models.Model):
    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    question = models.ForeignKey('Question', on_delete=models.CASCADE,
                                 related_name='answers', verbose_name='Вопрос')
    content = models.TextField(max_length=200, verbose_name='Содержание')
    correct = models.BooleanField(verbose_name='Верный ответ')
