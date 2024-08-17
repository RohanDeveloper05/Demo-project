from django.shortcuts import render
from django.http import HttpResponse
import psutil

def home(requst):
    return HttpResponse("Hello Everyone")
# Create your views here.
