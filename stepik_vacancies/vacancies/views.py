from django.shortcuts import render
from django.views import View
# Create your views here.


class MainView(View):

    def get(self, request):

        return render(request, 'index.html', {})


class VacanciesFull(View):

    def get(self, request):

        return render(request, 'vacancies.html', {})


class Vacancy(View):

    def get(self, request, id):

        return render(request, 'vacancy.html', {})


class VacanciesDirection(View):

    def get(self, request, direction):

        return render(request, 'vacancies.html', {})


class Company(View):

    def get(self, request, id):

        return render(request, 'company.html', {})






