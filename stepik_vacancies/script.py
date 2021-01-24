import os

import django

os.environ["DJANGO_SETTINGS_MODULE"] = 'stepik_vacancies.settings'
django.setup()

from vacancies import models
from vacancies import data
from authentication.models import RegisterModel



if __name__ == '__main__':

    test = models.Vacancy.objects.all().exists()
    if test is False:
        for specialty in data.specialties:
            specialties = models.Specialty.objects.create(
                code=specialty['code'],
                title=specialty['title']
            )
        for company in data.companies:
            companies = models.Company.objects.create(
                name=company['title'],
                location=company['location'],
                description=company['description'],
                employee_count=company['employee_count'],
            )
        for job in data.jobs:
            vacancy = models.Vacancy.objects.create(
                title=job['title'],
                specialty=models.Specialty.objects.get(code=job['specialty']),
                company=models.Company.objects.get(id=job['company']),
                skills=job['skills'],
                description=job['description'],
                salary_min=job['salary_from'],
                salary_max=job['salary_to'],
                published_at=job['posted'],
            )
    RegisterModel.objects.all().delete()
