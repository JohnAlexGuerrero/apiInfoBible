from django.shortcuts import redirect, render

from bookdata.models import Book

def home(request):
    template_name = "home/index.html"
    context = {}
    
    return render(request, template_name, context)