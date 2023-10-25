from django.contrib.auth.models import User
from django.db import models


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            status=Quiz.Status.PUBLISHED)


class Quiz(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0
        PUBLISHED = 1
        DELETED = 2

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'

    def count_likes(self):
        return self.interactions.filter(
            reaction=UserQuizInteraction.QuizReaction.LIKE).count()

    def count_dislikes(self):
        return self.interactions.filter(
            reaction=UserQuizInteraction.QuizReaction.DISLIKE).count()

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
    tags = models.ManyToManyField('Tag', related_name='quizzes',
                                  verbose_name='Тэги')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title


class Question(models.Model):
    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,
                             related_name='questions', verbose_name='Квиз')
    content = models.TextField(max_length=3000, verbose_name='Содержание')


class Answer(models.Model):
    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name='answers', verbose_name='Вопрос')
    content = models.TextField(max_length=200, verbose_name='Содержание')
    correct = models.BooleanField(verbose_name='Верный ответ')


class Tag(models.Model):
    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    title = models.CharField(max_length=100, unique=True, verbose_name='Имя')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Слаг')

    def __str__(self):
        return self.title


class UserQuizInteraction(models.Model):
    class QuizStatus(models.IntegerChoices):
        NOT_STARTED = 0
        STARTED = 1
        FINISHED = 2

    class QuizReaction(models.IntegerChoices):
        DISLIKE = 0
        LIKE = 1

    class Meta:
        verbose_name = 'Quiz Interaction'
        verbose_name_plural = 'Quiz Interactions'
        constraints = [
            models.UniqueConstraint(fields=['user', 'quiz'],
                                    name='unique_quiz_interaction'),
        ]

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='quiz_interactions',
                             verbose_name='Пользователь')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,
                             related_name='interactions',
                             verbose_name='Квиз')
    status = models.IntegerField(choices=QuizStatus.choices,
                                 verbose_name='Статус',
                                 default=QuizStatus.NOT_STARTED)
    step = models.IntegerField(default=0, verbose_name='Шаг')
    reaction = models.IntegerField(choices=QuizReaction.choices,
                                   verbose_name='Реакция', null=True,
                                   blank=True)


class Comment(models.Model):
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def count_likes(self):
        return self.comment_interactions.filter(
            reaction=UserCommentInteraction.CommentReaction.LIKE).count()

    def count_dislikes(self):
        return self.comment_interactions.filter(
            reaction=UserCommentInteraction.CommentReaction.DISLIKE).count()

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                             related_name='comments',
                             verbose_name='Пользователь')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,
                             related_name='comments',
                             verbose_name='Квиз')
    content = models.TextField(max_length=1000, verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Создано')
    edited_at = models.DateTimeField(auto_now=True,
                                     verbose_name='Изменено')


class UserCommentInteraction(models.Model):
    class CommentReaction(models.IntegerChoices):
        DISLIKE = 0
        LIKE = 1

    class Meta:
        verbose_name = 'Comment interaction'
        verbose_name_plural = 'Comment interactions'
        constraints = [
            models.UniqueConstraint(fields=['user', 'comment'],
                                    name='unique_comment_interaction'),
        ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                             related_name='comment_interactions',
                             verbose_name='Пользователь')

    comment = models.ForeignKey(Comment, on_delete=models.CASCADE,
                                related_name='comment_interactions',
                                verbose_name='Коммент')

    reaction = models.IntegerField(choices=CommentReaction.choices,
                                   verbose_name='Реакция', null=True,
                                   blank=True)
