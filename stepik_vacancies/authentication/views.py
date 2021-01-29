from django.shortcuts import render, redirect
from django.views import View

from . import form, models


class Login(View):

    def get(self, request):
        user = models.RegisterModel.objects.filter(authorized=True)
        print(len(user), user)
        if len(user) == 1:

            return redirect('my_company')
        return render(request, 'authentication/login.html', {'form': form.LoginForm})

    def post(self, request):

        post = request.POST
        print(post)
        auth = models.RegisterModel.objects.filter(name=post['login'], password=post['password'])

        if len(auth) == 1:

            auth[0].authorized = True
            auth[0].save()
            return redirect('my_company')

        return render(request, 'authentication/login.html', {'form': form.LoginForm})


class Register(View):

    def get(self, request):
        print(form.RegisterForm)
        return render(request, 'authentication/register.html', {'form': form.RegisterForm})

    def post(self, request):
        post = request.POST
        duble_login = models.RegisterModel.objects.filter(login=post['login']).exists()
        if duble_login is True:
            return redirect('register')
        reg = models.RegisterModel(login=post['login'], name=post['name'], surname=post['surname'], password=post['password'])
        reg.save()

        return redirect('login')



class Logout(View):

    def get(self, request):
        users = models.RegisterModel.objects.filter(authorized=True)
        print(users)
        for auth in users:
            auth.authorized = False
            auth.save()

        return redirect('home')
