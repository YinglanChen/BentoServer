from django.http import HttpResponse
from django.core import serializers
from .models import *
# Create your views here.


def foo(request):
    print(request)
    return HttpResponse("hello from foo")

