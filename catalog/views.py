from django.shortcuts import render
from .forms import FirstForm
from .forms import SecondForm

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