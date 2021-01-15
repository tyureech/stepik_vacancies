from django.shortcuts import render
from django.views import View

from . import models


class MainView(View):

    def get(self, request):

        context = {
            'specialties': models.Specialty.objects.all(),
            'companies': models.Company.objects.all()
        }

        return render(request, 'index.html', context=context)


class VacanciesAll(View):

    def get(self, request):

        vacancies = models.Vacancy.objects.all()
        number_vacancies = len(vacancies)

        context = {
            'vacancies': vacancies,
            'specialty_name_rus': 'Все вакансии',
            'number_vacancies': number_vacancies

        }

        return render(request, 'vacancies.html', context=context)


class Vacancy(View):

    def get(self, request, id):

        vacancy = models.Vacancy.objects.get(id=id)
        list_tetx = vacancy.description.split()
        print(list_tetx)

        context = {
            'vacancy': vacancy,
        }

        return render(request, 'vacancy.html', context=context)


class VacanciesDirection(View):

    def get(self, request, direction):

        specialty_name_rus = models.Specialty.objects.filter(code=direction)
        vacancies = models.Vacancy.objects.filter(specialty__code=direction)
        number_vacancies = len(vacancies)
        print(vacancies)


        context = {
            'specialty_name_rus': specialty_name_rus[0].title,
            'vacancies': vacancies,
            'number_vacancies': number_vacancies
        }

        return render(request, 'vacancies.html', context=context)


class Company(View):

    def get(self, request, id):

        company = models.Company.objects.get(id=id),
        vacancies = models.Vacancy.objects.filter(company=id)
        numbers_vacancies = len(vacancies)

        context = {
            'company': company[0],
            'vacancies': vacancies,
            'numbers_vacancies': numbers_vacancies
        }

        return render(request, 'company.html', context=context)
