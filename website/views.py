from django.shortcuts import render
from website.forms import CostumerForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def costumer(request):
    formulario = Co(request.POST or None)
    msg = ''
    if formulario.is_valid(): # Verifica se é valido
        formulario.save() # Salva as informações
        formulario = CostumerForm()
        msg = 'Pedido realizado com sucesso!' # Só cria a msg se estiver dentro do if

    contexto = {
        'form' : formulario,
        'msg' : msg
    }
    return render(request, 'costumer.html', contexto)

def client(request):
    return render(request, 'client.html')