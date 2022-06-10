from django.shortcuts import render
from .forms import SRC_FORMS
# Create your views here.

def form_view(request):
    context = {"form":SRC_FORMS()}

    return render(request,"index.html",context)
