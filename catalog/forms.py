from django import forms


class FirstForm(forms.Form):
    name = forms.CharField()
    birth = forms.DateField(widget = forms.SelectDateWidget)
    telegram = forms.CharField()
    phone = forms.CharField()
    inf = forms.CharField()

class SecondForm(forms.Form):
    name = forms.CharField()




