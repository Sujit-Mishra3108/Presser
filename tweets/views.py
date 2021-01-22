from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *ags,**kwargs):
    return HttpResponse("<h2>Hello World</h2>")
