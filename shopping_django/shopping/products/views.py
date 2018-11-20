from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import product_details, customer


def productView(request):
    #renders the products.html
    productObjects=product_details.objects.all()
    return render(request,'products.html',{'product_details':productObjects})

def homeView(request):
    #renders the products.html
    
    return render(request,'home.html')

def customerView(request):
    #renders the products.html
    customerObjects=customer.objects.all()
    return render(request,'customers.html',{'customer':customerObjects})


def addProduct(request):
   # category=request.POST.get('va')
    volPlus=int(request.POST['volPlus'])
    volUNLD=int(request.POST['volUNLD'])
    volSUPER=int(request.POST['volSUPER'])
    SUPER=int(request.POST['SUPER'])
    volCDIESEL=int(request.POST['volCDIESEL'])
    CDIESEL=int(request.POST['CDIESEL'])
    volRDIESEL=int(request.POST['volRDIESEL'])
    RDIESEL=int(request.POST['RDIESEL'])
    OIL=int(request.POST['OIL'])
    MISC=int(request.POST['MISC'])
    TAX=int(request.POST['TAX'])
    add_prod = product_details(productName=request.POST['productName'],
                                volPlus=request.POST['volPlus'],
                                volUNLD=request.POST['volUNLD'],
                                volSUPER=request.POST['volSUPER'],
                                SUPER=request.POST['SUPER'],
                                volCDIESEL=request.POST['volCDIESEL'],
                                CDIESEL=request.POST['CDIESEL'],
                                volRDIESEL=request.POST['volRDIESEL'],
                                RDIESEL=request.POST['RDIESEL'],
                                OIL=request.POST['OIL'],
                                MISC=request.POST['MISC'],
                                TAX=request.POST['TAX'],
                                AMT_TOTAL=volPlus+volUNLD+volSUPER+SUPER+volCDIESEL+CDIESEL+volRDIESEL+RDIESEL+OIL+MISC+TAX
                                )
    
    add_prod.save()
    return HttpResponseRedirect('/products/')
    #db.connection.close_all()
def addCustomer(request):
    add_cus=customer(customerName = request.POST['customerName'],
                        phoneNumber = request.POST['phoneNumber'],
                        address = request.POST['address'],
                        pinCode = request.POST['pinCode'])
    add_cus.save()
    
    return HttpResponseRedirect('/customer/')





