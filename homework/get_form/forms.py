from django import forms


class InputForm(forms.Form):
    '''
    первоначальный ввод, который необходимо провалидировать
    '''
    text_input1 = forms.CharField()
    text_input2 = forms.CharField()
    text_input3 = forms.CharField()
    text_input4 = forms.CharField()
