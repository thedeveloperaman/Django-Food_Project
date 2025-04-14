from django.shortcuts import render, redirect, get_object_or_404
from .models import FoodMenu
from .forms import FoodMenuForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    items = FoodMenu.objects.all()
    return render(request,'myfood/home.html', {'items':items})

@login_required
def additem(request):
    form = FoodMenuForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:home')
    return render(request, 'myfood/additemForm.html', {'form':form})

@login_required
def details(request, id):
    item = FoodMenu.objects.get(pk=id)
    return render(request, 'myfood/details.html', {'item':item})

def logout(request):
    logout = True
    return render(request,'myfood/home.html', {'logout':logout})