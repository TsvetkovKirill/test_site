# Generated by Django 4.2.1 on 2023-10-25 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_test', '0002_alter_quiz_options_alter_quiz_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=1000, verbose_name='Содержание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('edited_at', models.DateTimeField(auto_now=True, verbose_name='Изменено')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main_test.quiz', verbose_name='Квиз')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Имя')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='UserQuizInteraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Not Started'), (1, 'Started'), (2, 'Finished')], default=0, verbose_name='Статус')),
                ('step', models.IntegerField(default=0, verbose_name='Шаг')),
                ('reaction', models.IntegerField(blank=True, choices=[(0, 'Dislike'), (1, 'Like')], null=True, verbose_name='Реакция')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interactions', to='main_test.quiz', verbose_name='Квиз')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_interactions', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Quiz Interaction',
                'verbose_name_plural': 'Quiz Interactions',
            },
        ),
        migrations.CreateModel(
            name='UserCommentInteraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction', models.IntegerField(blank=True, choices=[(0, 'Dislike'), (1, 'Like')], null=True, verbose_name='Реакция')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_interactions', to='main_test.comment', verbose_name='Коммент')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment_interactions', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Comment interaction',
                'verbose_name_plural': 'Comment interactions',
            },
        ),
        migrations.AddField(
            model_name='quiz',
            name='tags',
            field=models.ManyToManyField(related_name='quizzes', to='main_test.tag', verbose_name='Тэги'),
        ),
        migrations.AddConstraint(
            model_name='userquizinteraction',
            constraint=models.UniqueConstraint(fields=('user', 'quiz'), name='unique_quiz_interaction'),
        ),
        migrations.AddConstraint(
            model_name='usercommentinteraction',
            constraint=models.UniqueConstraint(fields=('user', 'comment'), name='unique_comment_interaction'),
        ),
    ]
