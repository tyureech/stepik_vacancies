from django.urls import path

from . import views


urlpatterns = [
    path('mycompany/<str:user>', views.MyCompanyEdit.as_view(), name='my_company'),
    path('mycompany/vacancies', views.MyVacancies.as_view(), name='my_vacancies'),
    path('mycompany/vacancies/<int:id>', views.MyVacancy.as_view(), name='my_vacancy'),


]
