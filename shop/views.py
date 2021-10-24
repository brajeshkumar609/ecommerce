from django.shortcuts import render
from shop.models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    products=Product.objects.all()
    item_name=request.GET.get('item_name')
    if item_name!='' and item_name is not None:
        products=products.filter(title__icontains=item_name)
    paginator=Paginator(products,4)
    page=request.GET.get('page')
    products=paginator.get_page(page)

    return render(request, "index.html", {'product':products})
def details(request,id):
    product1=Product.objects.get(id=id)
    return render(request,"details.html", {'product1':product1})
