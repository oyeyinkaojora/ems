from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Products,Order,Customer
from .forms import OrderForm,CreateUserForm
from django.forms import inlineformset_factory
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,"Account was created for" + user)
            return redirect('login')
    context ={'form':form}
    return render(request, 'accounts/register.html',context)

def loginPage(request):
    if request.method == 'POST':
       username = request.POST.get('username') 
       password = request.POST.get('password') 

       user = authenticate(request, username = username , password = password)
       if user is not None:
          login(request,user)
          return redirect('home')
       else:
           messages.info(request,"Username or Password is incorrect")
    context ={}
    return render(request, 'accounts/login.html',context)

def logoutUser(request):
    logout(request)
    return render(request, 'accounts/logout.html',context)

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all() 

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders':orders,
        'customers':customers,
        'total_customers':total_customers,
        'total_orders':total_orders,
        'delivered':delivered,
        'pending':pending
    }
    return render(request, 'accounts/dashboard.html',context)

def products(request):
    products = Products.objects.all()
    context = {'products':products}
    return render(request, 'accounts/products.html',context)

def customer(request,pk_test):
    customers = Customer.objects.get(id=pk_test)
    orders = customers.order_set.all()
    orders_count = orders.count()

    myFilter = OrderFilter(request.GET,queryset=orders)
    orders = myFilter.qs

    context= {
        'customers':customers,
        'orders':orders,
        'orders_count': orders_count,
        'myFilter': myFilter ,
    }   
    return render(request, 'accounts/customers.html',context)

def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Order,fields=('products','status'),extra=10)
    customers = Customer.objects.get(id=pk)
    # the query set is added so that it can stop the orders on ground from showing
    formset= OrderFormSet(queryset=Order.objects.none(),instance=customers)
    #google what initial means
    #form = OrderForm(initial={'customer':customers})
    if request.method == "POST":
       formset= OrderFormSet(request.POST,instance=customers) 
       if formset.is_valid():
           formset.save()
           return redirect('/') 
    context ={
        'formset':formset,
        'customers':customers
    }
    return render(request,'accounts/order_form.html',context)   


def updateOrder(request, pk):
    order  = Order.objects.get(id=pk)
    # the word instance will generate a prefilled form 
    form = OrderForm(instance=order)
    if request.method == "POST":
       form = OrderForm(request.POST,instance=order)
       if form.is_valid():
           form.save()
           return redirect('/') 

    context ={
        'form':form
    }
    return render(request,'accounts/order_form.html',context)


def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/') 
    context = {
       'item':order
    }
    return render(request,'accounts/delete.html',context)
