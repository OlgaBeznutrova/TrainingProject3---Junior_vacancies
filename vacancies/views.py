from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import get_list_or_404
from .models import Specialty, Vacancy, Company
from django.db.models import Count
from django.http import Http404, HttpResponseNotFound, HttpResponseServerError


class HomePageView(TemplateView):
    template_name = "vacancies/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context["specialties"] = Specialty.objects.annotate(vacancies_count=Count('vacancies'))
        context["companies"] = Company.objects.annotate(vacancies_count=Count('vacancies'))
        return context


class ListVacanciesView(ListView):
    model = Vacancy

    def get_context_data(self, **kwargs):
        context = super(ListVacanciesView, self).get_context_data(**kwargs)
        context["title"] = "Все вакансии"
        return context


class ListCategoryView(ListView):
    model = Vacancy

    def get_context_data(self, **kwargs):
        context = super(ListCategoryView, self).get_context_data(**kwargs)
        context["title"] = Specialty.objects.get(code=self.kwargs["pk"]).title
        context["object_list"] = Vacancy.objects.filter(specialty__title=context["title"])
        return context


class ListCompanyView(ListView):
    template_name = "vacancies/company.html"


class DetailVacancyView(DetailView):
    model = Vacancy


def custom_handler404(request, exception):
    return HttpResponseNotFound("Ресурс не найден!")


def custom_handler500(request):
    return HttpResponseServerError("Ошибка сервера!")