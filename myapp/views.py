from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def trial(request):
    return HttpResponse('Congrats, Project is live')

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'myapp/home.html')

def profile(request):
    name='Hari'
    return render(request,'myapp/profile.html',{'name':name})