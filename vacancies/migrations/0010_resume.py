# Generated by Django 3.1.7 on 2021-05-28 03:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacancies', '0009_auto_20210527_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('status', models.CharField(choices=[
                    ('LF', 'Ищу работу'),
                    ('NLF', 'Не ищу работу'),
                    ('CO', 'Рассматриваю предложения'),
                ], default='LF', max_length=30, verbose_name='Готовность к работе')),
                ('salary', models.PositiveIntegerField(verbose_name='Вознаграждение')),
                ('education', models.CharField(max_length=255, verbose_name='Образование')),
                ('experience', models.TextField(max_length=1000, verbose_name='Опыт работы')),
                ('portfolio', models.FileField(
                    blank=True,
                    upload_to='portfolio/%Y/%m/%d',
                    verbose_name='Портфолио',
                ),
                 ),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('specialty', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name='resumes',
                    to='vacancies.specialty'),
                 ),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL,
                    verbose_name='Пользователь',
                ),
                 ),
            ],
            options={
                'verbose_name': 'Резюме',
                'verbose_name_plural': 'Резюме',
            },
        ),
    ]
