from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import FoodMenu
from .forms import FoodMenuForm
# Create your views here.
def home(request):
    items = FoodMenu.objects.all()
    
    return render(request,'myfood/home.html', {'items':items})

def additem(request):
    form = FoodMenuForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:home')
    return render(request, 'myfood/additemForm.html', {'form':form})

def details(request, id):
    item = FoodMenu.objects.get(pk=id)
    return render(request, 'myfood/details.html', {'item':item})

def logout(request):
    logout = True
    return render(request,'food:home')