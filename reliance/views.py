from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *

def home(request):
    order=Order.objects.all()
    customers=Customer.objects.all()

    total_customers=customers.count()
    total_orders=order.count()
    delivered=Order.objects.filter(status='Delivered').count()
    pending=Order.objects.filter(status='Pending').count()
    context={'orders':order,'customers':customers,
           'total_orders':total_orders,'delivered':delivered,
             'pending':pending,'total_customers':total_customers
                 }
    return render(request,'accounts/dashboard.html',context)

def products(request):
    products=Product.objects.all()
    return render(request,'accounts/products.html',{'products':products})

def customer(request,pk):
    customer =Customer.objects.get(id=pk)
    orders=customer.order_set.all()
    order_count=orders.count()
    context={
'customer':customer,'orders':orders,'order_count':order_count

    }
    return render(request,'accounts/profile.html',context)

def createOrder(request):
    form=OrderForm()
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')

    context={'form':form}
    return render(request,'accounts/order_form.html',context)

def updateOrder(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/home')
    context={'form':form}
    return render(request,'accounts/order_form.html',context)