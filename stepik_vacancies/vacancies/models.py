from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):

    name = models.CharField(max_length=30)
    location = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='MEDIA_COMPANY_IMAGE_DIR')
    description = models.TextField()
    employee_count = models.IntegerField()
    owner = models.ManyToManyField(User, related_name="User")
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


class RegisterModel(models.Model):

    login = models.CharField("Логин", max_length=20)
    name = models.CharField("Имя", max_length=20)
    surname = models.CharField("Фамилия", max_length=20)
    password = models.CharField("Пароль", max_length=20)


# code = Specialty.objects.all()
# print(code[1].code)

# specialty = Specialty(code='asd', title='asdasd')
# Specialty.objects.all().delete()
