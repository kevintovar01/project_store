from django.shortcuts import render
from .models import Service
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def services(request):
    
    services = Service.objects.all()
    
    return render(request,'services/services.html', {'services':services})