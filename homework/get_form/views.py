from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from . import forms
from . import models
from icecream import ic
import re
import datetime


# f_name1=value1&f_name2=value2

# Create your views here.

class Validator:
    '''
    получаем список из заполненых ячеек формы для валидации,
    возиращаем словарь,
    ключ - поле модели
    значение - валидное, либо "None"
    '''

    def __init__(self, list_form):
        self.list_form = list_form
        self.result = dict()

    def _validate_email(self, email: str) -> str:
        re_email = "^[A-Za-z0-9][A-Za-z0-9\.-_]*[A-Za-z0-9]*@([A-Za-z0-9]+([A-Za-z0-9-]*[A-Za-z0-9]+)*\.)+[A-Za-z]*$"
        if bool(re.fullmatch(re_email, email)):
            return email
        return

    def _validate_phone(self, phone: str) -> str:
        re_phone = "^(\+7)[ ](\d{3})[ ](\d{3})[ ](\d{2})[ ](\d{2})$"
        if bool(re.fullmatch(re_phone, phone)):
            return phone
        return

    def _validate_date(self, date: str) -> datetime:
        try:
            date1 = datetime.datetime.strptime(date, '%d.%m.%Y')
            return date1
        except ValueError:
            try:
                date2 = datetime.datetime.strptime(date, '%Y.%m.%d')
                return date2
            except ValueError:
                return

    def _validate(self):
        for field in self.list_form:
            field = field.strip()

            if email := self._validate_email(email=field):
                self.result['email'] = email
                continue
            elif 'email' not in self.result.keys():
                self.result['email'] = None

            if phone := self._validate_phone(phone=field):
                self.result['phone'] = phone
                continue
            elif 'phone' not in self.result.keys():
                self.result['phone'] = None

            if data := self._validate_date(date=field):
                self.result['data'] = data.date()
                continue
            elif 'data' not in self.result.keys():
                self.result['data'] = None

            self.result['text'] = field

    def run(self) -> dict:
        self._validate()
        return self.result


class Index(View):

    def get(self, request):
        form = forms.InputForm
        data = {'form': form,
                }
        result = render(request=request,
                        template_name='get_form/index.html',
                        context=data)
        return result

    def post(self, request):
        form = forms.InputForm(request.POST)
        if form.is_valid():
            valid_date = Validator(list_form=form.cleaned_data.values()).run()

            result_date_model = models.GetForm(
                email=valid_date.get('email'),
                phone=valid_date.get('phone'),
                date=valid_date.get('data'),
                text=valid_date.get('text'),
            )
            result_date_model.save()
            return HttpResponseRedirect('/get_form/done')
        else:
            ic(form, 'no valid')
            return HttpResponseRedirect('/get_form/no_done')


class ShowModelGetForm(View):
    def get(self, request):
        fields = models.GetForm.objects.all()
        data = {'fields': fields}
        result = render(request=request,
                        template_name='get_form/show_model_getform.html',
                        context=data)
        return result


def done(request):
    return render(request=request, template_name='get_form/done.html')


def no_done(request):
    return render(request=request, template_name='get_form/no_done.html')
