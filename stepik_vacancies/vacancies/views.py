from django.shortcuts import render
from django.views import View
from django.http import HttpResponseNotFound, HttpResponseServerError
from bs4 import BeautifulSoup

from . import models


def custom_handler404(request, exception):
    return HttpResponseNotFound("Нет такой страницы")


def custom_handler500(request):
    return HttpResponseServerError("Ошибка на сервере")


class MainView(View):

    def get(self, request):
        print(request.POST)
        specialties = models.Specialty.objects.all()
        companies = models.Company.objects.all()
        vacancies = models.Vacancy.objects.all()

        for specialty in specialties:
            nums = len(vacancies.filter(specialty__code=specialty.code))
            specialty.nums_vacancies = nums
            specialty.save()
            # print(specialty.nums_vacancies)
        print(specialty.picture)

        for company in companies:
            nums = len(vacancies.filter(company__id=company.id))
            company.nums_vacancies = nums
            company.save()
            # print(company.nums_vacancies)

        context = {
            'specialties': models.Specialty.objects.all(),
            'companies': models.Company.objects.all(),
        }

        return render(request, 'index.html', context=context)

    def post(self, request):
        print(request.POST)



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
        parser = BeautifulSoup(vacancy.description, 'lxml')
        teg_str_space_list = parser.prettify().split('\n')
        teg_str_list = []
        for teg_str_space in teg_str_space_list:
            teg_str_list.append(teg_str_space.strip())

        dict_start_finish = {
            'start': '',
            'finish': ''
        }
        dict_list = {

        }
        back_step = teg_str_list.pop(0)

        for step in teg_str_list:

            if step != '<b>' and back_step == '<p>':
                if dict_start_finish['start'] == '':
                    dict_start_finish['start'] = step
                elif dict_start_finish['finish'] == '':
                    dict_start_finish['finish'] = step

            elif back_step == '<b>':
                name_list = step
                dict_list[name_list] = []
            elif back_step == '<li>':
                dict_list[name_list].append('• ' + step[0].capitalize() + step[1:])
            back_step = step

        context = {
            'vacancy': vacancy,
            'dict_list': dict_list,
            'start_finish': dict_start_finish
        }

        return render(request, 'vacancy.html', context=context)


class VacanciesDirection(View):

    def get(self, request, direction):

        specialty_name_rus = models.Specialty.objects.get(code=direction)
        vacancies = models.Vacancy.objects.filter(specialty__code=direction)
        number_vacancies = len(vacancies)

        context = {
            'specialty_name_rus': specialty_name_rus.title,
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


class SendVacancy(View):

    def get(self, request, id):
        return render(request, 'sent.html', {})
