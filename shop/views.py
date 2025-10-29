from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('hello from home')


def check_age(request, age):
    if age >= 18:
        return HttpResponse('older ')
    
    else:
        return HttpResponse('young')


def region(request,region):
    uzbekistan = ("Toshkent", "Toshkent viloyati", "Andijon", "Fargona", "Namangan",
    "Sirdaryo", "Jizzax", "Samarqand", "Qashqadaryo", "Surxondaryo",
    "Navoiy", "Buxoro", "Xorazm", "Qoraqalpogiston Respublikasi")
    
    if region in uzbekistan:
        return HttpResponse(f' {region} in Uzbekistan')
    
    else:
        return HttpResponse(f' {region} is not in Uzbekistan')
    


