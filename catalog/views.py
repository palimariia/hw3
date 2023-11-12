from django.shortcuts import render, redirect
from .forms import FirstForm, SecondForm
# from .forms import MyForm
# from .models import MyModel

# def index(request):
#     if request.method == 'POST':
#         form = MyForm(request.POST)
#         if form.is_valid():
#             request.session['data'] = form.cleaned_data
#             return redirect('index2')
#     else:
#         form = MyForm()
#     return render(request, 'index2.html', {'form': form})
#
# def index2(request):
#     if 'data' in request.session:
#         data = request.session.pop('data')
#         form = MyForm(initial=data)
#         if form.is_valid():
#             form.save()
#     else:
#         return redirect('index')
#     return render(request, 'index2.html', {'form': form})
#
#
#
# def save_data(request):
#     if request.method == 'POST':
#         form = MyForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success')  # Replace with a success page or URL
#     else:
#         form = MyForm()
#     return render(request, 'succes_page.html', {'form': form})

# Create your views here.
def index(request):
    if request.method == "POST":
        form = FirstForm(request.POST)
        form2 = SecondForm()
        form2['name'].initial = form["name"].value()
        return render(request, "index2.html", {"form": form2})

    else:
        form = FirstForm()
        return render(request, "index.html", {"form": form})

# def first_page(request):
#     if request.method == "POST":
#         form = FirstForm(request.POST)
#         if form.is_valid():
#             request.session['form_data'] = form.cleaned_data
#             return redirect('second_page')
#     else:
#         form = FirstForm()
#     return render(request, 'index.html', {'form': form})
#
# def second_page(request):
#     if request.method == "POST":
#         form = SecondForm(request.POST)
#         if form.is_valid():
#             form_data = request.session.get('form_data', {})
#             form_data.update(form.cleaned_data)
#             # сохранение данных или выполнение другой логики
#             del request.session['form_data']
#             return redirect('success_page')
#     else:
#         form = SecondForm()
#     return render(request, 'index2.html', {'form': form})
#
# def success_page(request):
#     return render(request, 'success_page.html')
