from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def jay(request):
    return HttpResponse('This is my string 1 application')