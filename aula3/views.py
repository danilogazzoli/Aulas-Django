from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


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

def show_code(request, code):
    html = f"<h1>O código é {code} </h1>"
    response = HttpResponse(html)
    return response

def go_cats(request, code):
    html = f"<h1>O código do cats {code} </h1>"
    return HttpResponseRedirect(f'https://http.cat/{code}')

def show_get_values(request):
    #import ipdb; ipdb.set_trace()
    nome = request.GET.get("nome", None)
    if nome is None:
        html = '<h1> Bem vindo usuário anônimo </h1>'
    else:
        html = f"<h1>Bem vindo {nome} </h1>"
    return HttpResponse(html)

@csrf_exempt
def show_post_values(request):
    head = ""
    if request.method == 'POST':
        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")
        head += f"<h1> bem vindo {nome} {sobrenome} </h1>"
    html = """
<form method=POST>
  <label for="nome">Nome:</label><br>
  <input type="text" id="nome" name="nome" value="John"><br>
  <label for="sobrenome">Sobrenome:</label><br>
  <input type="text" id="sobrenome" name="sobrenome" value="Doe"><br><br>
  <input type="submit" value="Enviar">
</form> 
    """
    html_to_response = head + html
    return HttpResponse(html_to_response)

def show_info(request):
    html = f"<h1> O browser atual é: {request.META['HTTP_USER_AGENT']} </h1>" \
           f"<h1> Caminho: {request.path}" \
           f"<h1> Host: {request.get_host()}" \
           f"<h1> Full Path: {request.get_full_path()}"\
           f"<h1> Is secure: {request.is_secure()}" \
           f"<h1> Idioma: {request.META['LANGUAGE']}"

    response = HttpResponse(html)
    return response
