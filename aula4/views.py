from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"alunos":["Danilo", "Eloísa", "Ivisson", "Tiago"]}
    return render(request, 'aula4/index.html', context=context)


