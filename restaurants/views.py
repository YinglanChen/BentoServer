from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def foo(request):
    print(request)
    return HttpResponse("hello from foo")
