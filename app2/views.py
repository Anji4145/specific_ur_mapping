from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first(request):
    return HttpResponse('<h2>your name</h2>')
def second(request):
    return HttpResponse('<marquee><h2>silent voice</h2></marquee>')
