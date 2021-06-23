from django.shortcuts import render
from .models import ProductModels
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def store(request):
    products = ProductModels.objects.all()
    return render(request,'store/store.html', {'products':products})
