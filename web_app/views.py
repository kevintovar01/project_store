from django.shortcuts import render


from  services.models import Service


def home(request):
    return render(request,'web_app/home.html')











