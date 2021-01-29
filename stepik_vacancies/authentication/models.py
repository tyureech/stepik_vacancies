from django.db import models


class RegisterModel(models.Model):

    login = models.CharField("Логин", max_length=20)
    name = models.CharField("Имя", max_length=20)
    surname = models.CharField("Фамилия", max_length=20)
    password = models.CharField("Пароль", max_length=20)
    authorized = models.BooleanField(default=False)
