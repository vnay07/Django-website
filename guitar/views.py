# This is User defined file having the function to load pages
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def courses(request):
    return render(request,'courses.html')

