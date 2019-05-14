from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def costumer(request):
    return render(request, 'costumer.html')

def client(request):
    return render(request, 'client.html')