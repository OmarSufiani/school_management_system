from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.



def marksheet(request):
    form=Markform
    marks=Mark.objects.all()
    context={'marks':marks}
    return render(request, 'marks.html',context) 

def homePage(request):
    return render(request, 'home.html')     