from django.urls import path

from .views.my_company import MyCompanyEdit, MyCompanyCreate
from .views.my_vacancies import MyVacancies, MyVacancy


urlpatterns = [
    path('mycompany/vacancies/', MyVacancies.as_view(), name='my_vacancies'),
    path('mycompany/vacancies/<int:id>', MyVacancy.as_view(), name='my_vacancy'),
    path('mycompany/', MyCompanyEdit.as_view(), name='my_company'),
    path('mycomapny/create_company/', MyCompanyCreate.as_view(), name='my_company_create'),
]
