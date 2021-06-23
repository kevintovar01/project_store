from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from  services.models import Service

@login_required
def home(request):
    return render(request,'web_app/home.html')
 










