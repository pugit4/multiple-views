from django.shortcuts import render

# Create your views here.
def unionbank(request):
    return render(request, 'union.html')

def canarabank(request):
    return render(request, 'canara.html')

def hdfcbank(request):
    return render(request, 'hdfc.html')

def idfcbank(request):
    return  render(request, 'idfc.html')