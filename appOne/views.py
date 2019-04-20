from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {'insert_me':'I am from appOne/index.html'}
    return render(request,'appOne/index.html',context=my_dict)

def help(request):
    helpdict = {'help_insert': 'Help From Views.py'}
    return render(request, 'appOne/help.html', context=helpdict)
