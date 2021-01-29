# from django.shortcuts import render, redirect
# from django.views import View
# from django.forms.models import model_to_dict
#
# from stepik_vacancies.my_company.forms import CompanyForm
# from vacancies.models import Company
# from authentication.models import RegisterModel
#
#
# class MyCompanyEdit(View):
#
#     def get(self, request, user):
#
#         test_login = RegisterModel.objects.filter(name=user).exists()
#
#         if test_login is False:
#             return redirect('login')
#
#         company = Company.objects.filter(owner__login=user).exists()
#         print("12312312", company)
#
#         if company is False:
#             return redirect('my_company_create', user)
#
#         company = Company.objects.filter(owner__login=user)[0]
#         print(company, '1aaaaaa')
#
#         company_dict_rus = {}
#
#         company_dict_rus['Название компании'] = company.name
#         company_dict_rus['Логотип'] = company.logo
#         company_dict_rus['География'] = company.location
#         company_dict_rus['Количесво человек в компании'] = company.employee_count
#         company_dict_rus['Информация о компании'] = company.description
#
#         context = {
#             'model': company_dict_rus,
#             'user': user
#         }
#         return render(request, 'my_company/company-edit.html', context=context)
#
#     def post(self, request, user):
#         new_data = request.POST
#         data = Company.objects.get(owner__login=user)
#         data.name = new_data["Название компании"]
#         data.location = new_data["География"]
#         data.employee_count = new_data["Количесво человек в компании"]
#         data.description = new_data["Информация о компании"]
#         data.save()
#         print(data)
#
#         context = {
#             'info': "Информация о компании обновлена",
#             'user': user,
#         }
#
#         return render(request, 'my_company/company-edit.html', context=context)
#
#
# class MyCompanyCreate(View):
#
#     def get(self, request, user):
#         print('123123')
#         return render(request, 'my_company/company-create.html', {'user': user})
#
#     def post(self, request, user):
#         user_data = RegisterModel.objects.filter(login=user)[0]
#         test = Company.objects.filter(owner__login=user).exists()
#         if test is False:
#             companies = Company.objects.create(
#                 name='...',
#                 location='...',
#                 description='...',
#                 employee_count=0,
#                 owner=user_data,
#             )
#         print(Company.objects.filter(owner__login=user))
#         return redirect('my_company', user)
#
#
#
# class MyVacancies(View):
#
#     def get(self, request):
#         return render(request, 'my_company/vacancy-list.html', {})
#
#
# class MyVacancy(View):
#
#     def get(self, request, id):
#         return render(request, 'my_company/vacancy-edit.html', {})


