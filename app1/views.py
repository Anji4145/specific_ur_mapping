from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first(request):
    return HttpResponse('<h2>weathering with you</h2>')
def second(request):
    return HttpResponse('<marquee><h2>garden of words</h2></marquee>')
