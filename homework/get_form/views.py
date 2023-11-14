from django.shortcuts import render


# f_name1=value1&f_name2=value2

# Create your views here.

def index(request):
    print(request.method)
    res = dict()
    if request.method == 'GET':
        res = request.GET
    elif request.method == 'GET':
        pass
    data = {'request': res}
    result = render(request=request,
                    template_name='get_form/index.html',
                    context=data)
    return result
