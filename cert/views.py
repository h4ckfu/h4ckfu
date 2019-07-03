from django.shortcuts import render
from .models import Cert

# Create your views here.
def cert(request):
    cert = Cert.objects
    return render(request, 'cert/cert.html', {'cert':cert})