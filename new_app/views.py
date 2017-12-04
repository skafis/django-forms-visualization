from django.shortcuts import render

# Create your views here.

def add_data(request):
    return render (request, "index.html")