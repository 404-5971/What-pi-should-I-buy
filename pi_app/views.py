from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mainpage(request):
    return HttpResponse("This is an html TEXT YO! Good bye world!")