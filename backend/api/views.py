from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
# Create your views here.

def login(request):
    return HttpResponse('Login')

