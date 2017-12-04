from django.shortcuts import render, redirect

from .forms import AddNumbersForm
# Create your views here.

def add_data(request):
    ctx = {}
    form = AddNumbersForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render (request, "index.html", ctx)
