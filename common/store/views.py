from typing import Any, Dict
from django.shortcuts import render
from .models import Product, Order, Category
from django.views.generic import ListView, DetailView
from .util import CategoryListMixin



class ProductListView(CategoryListMixin, ListView):
    model = Product

    def get_queryset(self):
        search_query = self.request.GET.get("search", None)
        if search_query:
            return self.model.objects.filter(title__icontains=search_query)
        return self.model.objects.all()
    


    

"""
def product_list(request):
    search_query = request.GET.get('search', None)
    if search_query:
        product_list = Product.objects.filter(title__icontains=search_query)
    else:
        product_list = Product.objects.all()
    return render(request, "store/product_list.html", context={'product_list' : product_list})
"""


class ProductDetailView(DetailView, CategoryListMixin):
    model = Product


"""
def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, "store/product_detail.html", context={'product': product})
"""


class CategoryDetailView(DetailView, CategoryListMixin):
    model = Category


"""
def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    return render(request, "store/category_detail.html", context={'category': category})
"""


def save_order(request):
    product = Product.objects.get(pk=request.POST["product_id"])
    order = Order()
    order.name = request.POST["user_name"]
    order.email = request.POST["user_email"]
    order.product = product
    order.save()

    return render(
        request,
        "store/save_order.html",
        context={"product": product, "name": request.POST["user_name"]},
    )



def index(request):
    #create
    #p = Product(title='ICL', price=1200, color_id=1, storage=256)
    #p.save()
    
    #p = Product.objects.create(title='HP', price=100, color_id=2, storage=256)
    
    #update
    #p = Product.objects.get(pk=9)
    #p.price += 10
    #p.save()

    #Product.objects.filter(pk = 9).update(price = 160)
    #p = Product.objects.get(pk=9)
    
    #destroy
    #Product.objects.get(pk=9).delete()
    #p = Product.objects.all()
    
    #get 
    #p = Product.objects.filter(title='ICL')


    #print(p)
    return render(request, 'store/product_list.html')