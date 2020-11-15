from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, ListView
from .forms import LoginForm, UploadFileForm
from .models import FileParse, FileResult, Billing
from django.contrib import auth
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist

class Index(View):
    template_name = 'pochta_main/index.html'
    context = {
        'title': 'Главная страница',
        'content': 'Это главная страница',
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.context)


class Login(View):
    template_name = 'pochta_main/login.html'
    message = ''
    context = {
        'title': 'Логин',
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
                return redirect( request.GET.get('next','/'))
            else:
                self.context['message'] = 'Ошибка авторизации'
        else:
            self.context['message'] = 'Ошибка формы'
        return render(request, self.template_name, context=self.context)


class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('index')


class Pass(View):
    template_name = 'pochta_main/pass.html'
    message = ''
    context = {
        'title': 'УПС! Заглушка',
        'message': '',
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.context)


class Upload(CreateView):
    model = FileParse
    form_class = UploadFileForm
    template_name = 'pochta_main/upload.html'
    success_url = reverse_lazy('upload')
    context = {
        'message': '',
        'title': 'Загрузить файл',
        'form': UploadFileForm(),
    }

    def get_context_data(self, **kwargs):
        context = super(Upload, self).get_context_data(**kwargs)
        context['title'] = self.context['title']
        return context


class Files(View):

    def get(self, request):
        files = FileParse.objects.all()
        return render(request, 'pochta_main/files.html', context={'files': files})


class Files_Detail(View):
    def get(self, request, pk):
        # id = self.request.query_params.get('id')
        try:
            fl = FileParse.objects.get(pk=pk)
            filename = fl.filename()
            fl_r = FileResult.objects.all().filter(file_source=pk)
        except ObjectDoesNotExist as e:
            return render(request, 'pochta_main/files_detail.html', context={'file_records': None, 'filename': filename, 'fl': pk})
        return render(request, 'pochta_main/files_detail.html', context={'file_records': fl_r,  'filename': filename})

class BillingView(View):
    context = {
        'message': 'Укажите период запроса',
        'title': 'Биллинг'
    }
    template_name = 'pochta_main/billing.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.context)

    def post(self, request, *args, **kwargs):
        date_begin = request.POST.get('date_begin')
        date_end = request.POST.get('date_end')
        bil = Billing.objects.get(date_req > date_begin).get(date_req < date_end)
        self.context['billing'] = bil
        return render(request, self.template_name, context=self.context)