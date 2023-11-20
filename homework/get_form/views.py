from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms


# f_name1=value1&f_name2=value2

# Create your views here.

def index(request):
    if request.method == 'POST':
        forms_ls = [forms.EmailForm(request.POST),
                    forms.PhoneForm(request.POST),
                    forms.DateForm(request.POST),
                    ]
        form = forms_ls[0]
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('/get_form/done')
    else:
        forms_ls = [forms.EmailForm(request.POST),
                    forms.PhoneForm(request.POST),
                    forms.DateForm(request.POST),
                    ]
        form = forms_ls[0]
    data = {'form': form,
            'method': request.method}
    result = render(request=request,
                    template_name='get_form/index.html',
                    context=data)
    return result


def done(request):
    return render(request=request, template_name='get_form/done.html')
