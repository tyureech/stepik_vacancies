from django.db import models
from django.contrib.auth.models import User

from authentication.models import RegisterModel



class Company(models.Model):

    name = models.CharField(verbose_name='Название компании', max_length=30)
    location = models.CharField('География', max_length=20)
    logo = models.ImageField('Логотип', upload_to='MEDIA_COMPANY_IMAGE_DIR')
    description = models.TextField()
    employee_count = models.IntegerField()
    owner = models.ForeignKey(RegisterModel, on_delete=models.CASCADE, related_name="user", blank=True, null=True)
    nums_vacancies = models.IntegerField(null=True)


class Specialty(models.Model):
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='speciality_images')
    nums_vacancies = models.IntegerField(null=True)


class Vacancy(models.Model):

    title = models.CharField(max_length=30)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()


class Application(models.Model):

    written_username = models.CharField(max_length=20)
    written_phone = models.IntegerField(max_length=11)
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="applications")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")


# code = Specialty.objects.all()
# print(code[1].code)

# specialty = Specialty(code='asd', title='asdasd')
# Specialty.objects.all().delete()
