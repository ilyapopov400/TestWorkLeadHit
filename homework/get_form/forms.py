from django import forms


class EmailForm(forms.Form):
    email = forms.EmailField()


class PhoneForm(forms.Form):
    phone = forms.CharField()


class DateForm(forms.Form):
    date = forms.DateField()
