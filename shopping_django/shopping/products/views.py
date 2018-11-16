from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import product_details


def productView(request):
    #renders the products.html
    productObjects=product_details.objects.all()
    return render(request,'products.html',{'product_details':productObjects})


def addProduct(request):
   # category=request.POST.get('va')
    add_prod = product_details(productName=request.POST['productName'],
                                produtID=request.POST['productID']
                                )
    add_prod.save()
    
    return HttpResponseRedirect('/products/')
    #db.connection.close_all()
