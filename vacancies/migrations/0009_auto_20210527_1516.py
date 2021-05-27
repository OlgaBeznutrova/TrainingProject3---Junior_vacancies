# Generated by Django 3.1.7 on 2021-05-27 03:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacancies', '0008_auto_20210521_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Кол-во просмотров'),
        ),
        migrations.AlterField(
            model_name='application',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='applications',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name='application',
            name='written_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='RU'),
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(max_length=1000, verbose_name='Информация о компании'),
        ),
        migrations.AlterField(
            model_name='company',
            name='employee_count',
            field=models.PositiveIntegerField(verbose_name='Кол-во сотрудников'),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(default='https://place-hold.it/100x60', upload_to='company_logo',
                                    verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название компании'),
        ),
        migrations.AlterField(
            model_name='company',
            name='owner',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name='Владелец',
            ),
        ),
    ]