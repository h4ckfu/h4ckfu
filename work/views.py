from django.shortcuts import render

from .models import Work

# Create your views here.
def work(request):
    work = Work.objects
    return render(request, 'work/work.html', {'work':work})

