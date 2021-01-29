from django.shortcuts import render, redirect
from django.views import View
from django.forms.models import model_to_dict

# from my_company.forms import CompanyForm
from vacancies.models import Company
from authentication.models import RegisterModel


class MyCompanyEdit(View):

    def get(self, request):

        user = RegisterModel.objects.filter(authorized=True)

        if len(user) == 0:
            return redirect('login')

        company = Company.objects.filter(owner__login=user[0].login)
        print("12312312", company)

        if len(company) == 0:
            return redirect('my_company_create')

        company = company[0]
        print(company, '1aaaaaa')

        company_dict_rus = {}

        company_dict_rus['Название компании'] = company.name
        company_dict_rus['Логотип'] = company.logo
        company_dict_rus['География'] = company.location
        company_dict_rus['Количесво человек в компании'] = company.employee_count
        company_dict_rus['Информация о компании'] = company.description

        context = {
            'model': company_dict_rus,
            'user': user[0],
            'active_company': 'active',
        }
        return render(request, 'my_company/company-edit.html', context=context)

    def post(self, request):
        new_data = request.POST
        user = RegisterModel.objects.get(authorized=True)
        data = Company.objects.get(owner__login=user.login)
        data.name = new_data["Название компании"]
        data.location = new_data["География"]
        data.employee_count = new_data["Количесво человек в компании"]
        data.description = new_data["Информация о компании"]
        data.save()
        print(data)

        context = {
            'info': "Информация о компании обновлена",
            'user': user,
        }

        return render(request, 'my_company/company-edit.html', context=context)


class MyCompanyCreate(View):

    def get(self, request):
        test_login = RegisterModel.objects.filter(authorized=True).exists()

        if test_login is False:
            return redirect('login')

        return render(request, 'my_company/company-create.html', {})

    def post(self, request):
        user_data = RegisterModel.objects.filter(authorized=True)[0]

        companies = Company.objects.create(
            name='...',
            location='...',
            description='...',
            employee_count=0,
            owner=user_data,
        )

        return redirect('my_company')
