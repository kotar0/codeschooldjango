from django.shortcuts import render
from .models import Person

# Create your views here.
def index(request):
    people = Preson.objects.all()
    return render(request, 'index.html', {'people':people})
