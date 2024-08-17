from django.shortcuts import render
from django.http import HttpResponse
import pyjokes

def home(requst):
    return HttpResponse(pyjokes.get_joke())
# Create your views here.
