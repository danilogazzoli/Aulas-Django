from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'aula6/index.html')

