from django.shortcuts import render
from website.forms import CostumerForm
from website.models import Costumer

# Create your views here.
def index(request):
    return render(request, 'index.html')

def costumer(request):
    formulario = CostumerForm(request.POST or None)
    msg = ''
    if formulario.is_valid(): # Verifica se é valido
        formulario.save() # Salva as informações
        formulario = CostumerForm()
        msg = 'Cadastro feito com sucesso!' # Só cria a msg se estiver dentro do if

    contexto = {
        'form' : formulario,
        'msg' : msg
    }
    return render(request, 'costumer.html', contexto)

def client(request):
    val_localizacao = request.GET.get('localizacao')
    val_tipo = request.GET.get('tipo')
    if val_localizacao or val_tipo:
        customizadores = Costumer.objects.filter(endereco__contains = val_localizacao, descricao__contains = val_tipo)
    else:
        customizadores = Costumer.objects.all()
        # customizadores = Costumer.objects.filter(nome_empresa__contains = "Repara")

    contexto = {
        'customizadores' : customizadores
    }
    return render(request, 'client.html', contexto)