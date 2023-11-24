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
        self.re_email = "^[A-Za-z0-9][A-Za-z0-9\.-_]*[A-Za-z0-9]*@([A-Za-z0-9]+([A-Za-z0-9-]*[A-Za-z0-9]+)*\.)+[A-Za-z]*$"
        self.re_phone = "^(\+7)[ ](\d{3})[ ](\d{3})[ ](\d{2})[ ](\d{2})$"

    def _validate(self):
        for field in self.list_form:
            field = field.strip()

            if bool(re.fullmatch(self.re_email, field)):
                self.result['email'] = field
                continue
            elif 'email' not in self.result.keys():
                self.result['email'] = None

            if bool(re.fullmatch(self.re_phone, field)):
                self.result['phone'] = field
                continue
            elif 'phone' not in self.result.keys():
                self.result['phone'] = None

            try:
                date1 = datetime.datetime.strptime(field, '%d.%m.%Y')
                if 'data' not in self.result.keys():
                    self.result['data'] = date1
                    continue
            except ValueError:
                try:
                    date2 = datetime.datetime.strptime(field, '%Y.%m.%d')
                    if 'data' not in self.result.keys():
                        self.result['data'] = date2
                        continue
                except ValueError:
                    if 'data' not in self.result.keys():
                        self.result['data'] = None
                        continue

            self.result['text'] = field

    def run(self):
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
            ic(valid_date)
            return HttpResponseRedirect('/get_form/done')
        else:
            ic(form, 'no valid')
            return HttpResponseRedirect('/get_form/no_done')


def done(request):
    return render(request=request, template_name='get_form/done.html')


def no_done(request):
    return render(request=request, template_name='get_form/no_done.html')
