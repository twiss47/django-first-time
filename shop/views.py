from django.shortcuts import render, get_object_or_404
from .models import Person

def home(request):
    people = Person.objects.all()
    return render(request, 'index.html', {'people': people})

def person_detail(request, id):
    person = get_object_or_404(Person, id=id)
    return render(request, 'detail.html', {'person': person})
