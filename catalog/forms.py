from django import forms
# from .models import MyModel

# class MyForm(forms.ModelForm):
#     class Meta:
#         model = MyModel
#         fields = ('name', 'inf', 'birth', 'telegram', 'phone', 'course', 'faculty', 'program', 'work')

class FirstForm(forms.Form):
    name = forms.CharField()
    birth = forms.DateField(widget = forms.SelectDateWidget)
    telegram = forms.CharField()
    phone = forms.CharField()
    inf = forms.CharField()

class SecondForm(forms.Form):
    name = forms.CharField()
    inf = forms.CharField()
    course = forms.IntegerField()
    faculty = forms.CharField()
    program = forms.CharField()
    work = forms.CharField()



