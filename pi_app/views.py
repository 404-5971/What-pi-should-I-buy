from django.shortcuts import render
import random

def mainpage(request):
    template = 'index.html'
    randomVariable = random.choice(range(0, 10000))
    
    context = { 'test': randomVariable}
    return render(request, template, context)