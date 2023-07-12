from django.shortcuts import render, redirect
from django.utils.dateparse import parse_datetime
from django.db.models import Sum, F
from django.urls import reverse
from .models import Product

def home(request):
    existing_product = False
    new_product = Product()
    new_product.quantity = request.POST.get('quantity')
    new_product.name = request.POST.get("name")
    new_product.price = request.POST.get('price')
    if Product.objects.exists():
        products = Product.objects.all()
        for product in products:
            if product.name == new_product.name:
                if int(product.quantity) == int(new_product.quantity):
                    if float(product.price) == float(new_product.price):
                        existing_product = True
                        break

    print(existing_product)
    if existing_product == True:
        products = {
        'products': Product.objects.all()
    }
        return render(request,'products/home.html',products)  
    temp = request.POST.get("perishable")
    if temp == "1":
        new_product.perishable = True
    else:
        new_product.perishable = False
    tempDate = request.POST.get('expire')
    if tempDate:
        new_product.expire_date = tempDate
    else:
        new_product.expire_date = None
    if new_product.sales == 0:
        new_product.sales = None   
    has_null = check_print(new_product)
    if new_product.sales == None:
        new_product.sales = 0
    if has_null == False:
        new_product.save()
    products = {
        'products': Product.objects.all()
    }
    return render(request,'products/home.html',products)

def register(request):
    return render(request,'products/register.html')

def overall(request):
    most_sold = Product.objects.order_by('-sales').first()
    most_profit = Product.objects.annotate(profit=Sum(F('sales') * F('price'))).order_by('profit').last()
    total_sales = Product.objects.aggregate(total_quantity = Sum('sales'))
    total_profit = Product.objects.aggregate(profit_overall=Sum(F('sales') * F('price'))).get('profit_overall')
    overall = {
        'most_sold': most_sold,
        'most_profit': most_profit,
        'total_sales': total_sales['total_quantity'],
        'total_profit': total_profit
    }
    return render(request, 'products/overall.html',overall)

def update(request,param):
    my_param = request.GET.get('param')
    product = Product.objects.get(id_product=param)

    if request.method == 'POST':
        sales = request.POST.get('sales')
        quantity = request.POST.get('quantity')
        print(quantity)
        if sales != '':
            product.sales += int(sales)
            product.quantity -= int(sales)
        if quantity != '':
            product.quantity += int(quantity)
        product.save()
        return redirect(reverse('home'))

    updated={
        'param' : my_param,
        'product' : product
    }
    return render(request, 'products/update.html', updated)

def check_null_attributes(obj):  
    for attr, value in obj.__dict__.items():
        print(attr)
        print(value)
        print('-------------')
        if value is not None:
            return False
    return True

def check_print(obj):
    teste =  True
    for attr, value in obj.__dict__.items():
        if attr != '_state':
            if value is not None:
                if value is not False:
                    teste = False  
    return teste
        
        
            