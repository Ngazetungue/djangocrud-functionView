from django.shortcuts import render, redirect
from .models import Products
from .forms import ProductForm


# Create your views here.
def list_products(request):
    product = Products.objects.all()
    return render(request, 'products/list_products.html', {'product':product})

def create_products(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'products/create_products.html', {'form':form })

def update_product(request, id):
    product = Products.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'products/create_products.html', {'form':form, 'product':product })


def delete_product(request, id):
    product = Products.objects.get(id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('list_products')

    return render(request, 'products/delete_product.html',{'product':product})


