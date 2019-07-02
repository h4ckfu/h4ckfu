from django.shortcuts import render

from .models import Home

# Create your views here.
def home(request):
    home = Home.objects
    return render(request, 'home/home.html', {'home':home})
