from django.shortcuts import render
from . models import Product
# Create your views here.

def Home(request):
    pd = Product.objects.all()
    count = pd.count()
    return render(request, 'Store/index.html', {'pd':pd, 'count': count})

def Details(request, pk):
    info = Product.objects.filter(pk=pk)
    return render(request, 'Store/detail.html', {'info': info})

def Cart(request, pk):
    cr = Product.objects.filter(pk=pk)
    return render(request, 'Store/cart.html',{'cr': cr})