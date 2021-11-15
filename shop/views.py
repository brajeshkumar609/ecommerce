from django.shortcuts import redirect, render
from shop.models import Product, ring
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    products=Product.objects.all()
    item_name=request.GET.get('item_name')
    if item_name!='' and item_name is not None:
        products=products.filter(title__icontains=item_name)
    paginator=Paginator(products,12)
    page=request.GET.get('page')
    products=paginator.get_page(page)

    return render(request, "index.html", {'product':products})
def details(request,id):
    product1=Product.objects.get(id=id)
    return render(request,"details.html", {'product1':product1})
def home(request):
    return render(request, 'index.html')
def rings(request):
    rings=ring.objects.all()
    return render(request, 'ring.html',{'ring':rings})
def checkout(request):

    if request.method == 'POST':

        items =request.POST.get('items',"") #allow the null value thats why put the empty string ""
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total','')
        order_list = order( items = items,name = name, email = email, address = address, city = city, state = state, zipcode = zipcode,total = total)
        order_list.save()

    return render(request,'shop/checkout.html')
