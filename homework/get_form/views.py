from django.shortcuts import render


# Create your views here.

def index(request):
    result = render(request=request, template_name='get_form/index.html')
    return result
