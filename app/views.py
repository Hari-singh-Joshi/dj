from django.shortcuts import render

from .models import Product
def Homeview(request):
    return render(request,"home.html")

def CreateView(name, category, sku, description, price, stock_quantity):
    product = Product(
        name=name,
        category=category,
        sku=sku,
        description=description,
        price=price,
        stock_quantity=stock_quantity
    )
    product.save()
    return product

def SearchView(product_id):
    return Product.objects.get(id=product_id)

def UpdateView(product_id, **kwargs):
    Product.objects.filter(id=product_id).update(**kwargs)

def DeleteView(product_id):
    Product.objects.filter(id=product_id).delete()