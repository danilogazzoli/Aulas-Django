from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone


def index(request):
    html = f"<h1> Bem vindo: {timezone.now()} </h1>"
    response = HttpResponse(html)
    response['meu_header'] = 'Danilo2'
    response['ultimo_acesso'] = timezone.now()
    return response

def setacookie(request):
    response = HttpResponse()
    response.set_cookie("my_name", value="Danilo")
    return response

def redireciona(request):
    return HttpResponseRedirect('https://uol.com.br')