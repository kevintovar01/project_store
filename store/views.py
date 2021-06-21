from django.shortcuts import render
from .models import ProductModels

# Create your views here.


def store(request):
    products = ProductModels.objects.all()
    return render(request,'store/store.html', {'products':products})
