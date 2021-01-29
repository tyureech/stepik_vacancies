from django.shortcuts import render
from django.views import View
from bs4 import BeautifulSoup

from authentication.models import RegisterModel
from vacancies.models import Vacancy, Specialty


class MyVacancies(View):

    def get(self, request):

        user = RegisterModel.objects.get(authorized=True)
        vacancies = Vacancy.objects.filter(company__owner__login=user.login)

        context = {
            'vacancies': vacancies,
            'user': user,
            'active_vacancy': 'active',
        }

        return render(request, 'my_company/vacancy-list.html', context=context)


class MyVacancy(View):

    def get(self, request, id):

        user = RegisterModel.objects.get(authorized=True)
        vacancy = Vacancy.objects.get(id=id)
        teg_text = BeautifulSoup(vacancy.description, 'lxml')
        teg_text = teg_text.prettify().split('\n')

        context = {
            'specialties': Specialty.objects.all(),
            'vacancy': vacancy,
            'user': user,
            'active_vacancy': 'active',
        }
        return render(request, 'my_company/vacancy-edit.html', context=context)

    def post(self, request, id):

        print(request.POST)
        user = RegisterModel.objects.get(authorized=True)
        vacancy = Vacancy.objects.get(id=id)

        context = {
            'vacancy': vacancy,
            'active_vacancy': 'active',
            'specialties': Specialty.objects.all(),
            'user': user,
        }
        return render(request, 'my_company/vacancy-edit.html', context=context)
