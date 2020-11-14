from django.shortcuts import render, redirect
from django.views import View
from .forms import ProfileForm, LoginForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class index(View):
    template_name = 'pochta_main/index.html'
    context = {
        'title': 'Главная страница',
        'content': 'Это главная страница',
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.context)


class profile(View):
    template_name = 'pochta_main/profile.html'
    message = ''
    context = {
        'message': '',
        'form': ProfileForm(),
    }

    @method_decorator(login_required(login_url='login'))
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.context)

    @method_decorator(login_required(login_url='login'))
    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            self.context['message'] = 'Ошибка формы'
        return render(request, self.template_name, context=self.context)


class login(View):
    template_name = 'pochta_main/login.html'
    message = ''
    context = {
        'message': '',
        'form': LoginForm(),
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                self.context['message'] = 'Ошибка авторизации'
        else:
            self.context['message'] = 'Ошибка формы'
        return render(request, self.template_name, context=self.context)