from django.shortcuts import render
from django.views import View
from django.forms.models import model_to_dict

from .forms import CompanyForm
from vacancies.models import Company


class MyCompanyEdit(View):

    def get(self, request, user):
        company = Company.objects.get(id=2)
        company_dict_rus = {}
        company_dict_rus['Название компании'] = company.name
        company_dict_rus['Логотип'] = company.logo
        company_dict_rus['География'] = company.location
        company_dict_rus['Количесво человек в компании'] = company.employee_count
        company_dict_rus['Информация о компании'] = company.description

        context = {
            'model': company_dict_rus,
            'user': user
        }
        return render(request, 'my_company/company-edit.html', context=context)

    def post(self, request, user):
        new_data = request.POST
        data = Company.objects.get(name=new_data["Название компании"])
        data.name = new_data["Название компании"]
        data.location = new_data["География"]
        data.employee_count = new_data["Количесво человек в компании"]
        data.description = new_data["Информация о компании"]
        data.save()

        return render(request, 'my_company/company-edit.html', {'info': "Информация о компании обновлена"})




class MyVacancies(View):

    def get(self, request):
        return render(request, 'my_company/vacancy-list.html', {})


class MyVacancy(View):

    def get(self, request, id):
        return render(request, 'my_company/vacancy-edit.html', {})


