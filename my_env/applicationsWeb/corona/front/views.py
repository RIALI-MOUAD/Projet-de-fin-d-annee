from django.shortcuts import render
from .models import FrontHome
# Create your views here.



def fronthome(request):
    front=FrontHome.objects.all()
    context={
       'front':front;
    }
    return render(request, '../countries/templates/corona/home.html' ,context)
