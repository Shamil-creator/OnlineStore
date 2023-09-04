from django.shortcuts import render
from .models import Product, Category, Order


def product_list(request):
    search_query = request.GET.get('search', None)
    if search_query:
        product_list = Product.objects.filter(title__icontains=search_query)
    else:
        product_list = Product.objects.all()
    return render(request, "store/product_list.html", context={'product_list' : product_list})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, "store/product_detail.html", context={'product': product})

def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    return render(request, "store/category_detail.html", context={'category': category})

def save_order(request):
    product = Product.objects.get(pk=request.POST['product_id'])
    order = Order()
    order.name = request.POST['user_name']
    order.email = request.POST['user_email']
    order.product = product
    order.save()

    return render(request, 'store/product_list.html')