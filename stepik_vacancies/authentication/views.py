from django.shortcuts import render, redirect
from django.views import View

from . import form, models


class Login(View):

    def get(self, request):
        return render(request, 'authentication/login.html', {'form': form.LoginForm})

    def post(self, request):
        post = request.POST
        print(post)
        auth = models.RegisterModel.objects.filter(name=post['login'], password=post['password']).exists()
        if auth is True:
            return redirect('my_company', post['login'])
        return render(request, 'authentication/login.html', {'form': form.LoginForm})


class Register(View):

    def get(self, request):
        print(form.RegisterForm)
        return render(request, 'authentication/register.html', {'form': form.RegisterForm})

    def post(self, request):
        post = request.POST
        reg = models.RegisterModel(login=post['login'], name=post['name'], surname=post['surname'], password=post['password'])
        reg.save()

        return redirect('login')

