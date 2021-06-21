from django.shortcuts import render, redirect
from .car import Car
from store.models import ProductModels

# Create your views here.

def add_product(request, product_id):
    car = Car(request)
    product = ProductModels.objects.get(id=product_id)
    car.add(product=product)

    return redirect('store:store')


def delete_product(request, product_id):
    car = Car(request)
    product = ProductModels.objects.get(id=product_id)
    car.delete(product=product)
    return redirect('store:store')


def subtract_product(request, product_id):
    car = Car(request)
    product = ProductModels.objects.get(id=product_id)
    car.subtract_product(product=product)
    return redirect('store:store')


def clear_product(request):
    car = Car(request)
    car.clear()
    return redirect('store:store')


