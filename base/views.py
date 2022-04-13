from audioop import reverse
from accounts.models import User

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator 

from django.shortcuts import redirect, render
from base.models import *
# Create your views here.

def home(request):
    products=Products.objects.all()
    banner = Images.objects.get(name='banner-left')
    ban_rgt_one = Images.objects.get(name='banner-right-1')
    ban_rgt_two = Images.objects.get(name='banner-right-2')
    ban_rgt_three = Images.objects.get(name='banner-right-3')
    ban_rgt_four = Images.objects.get(name='banner-right-4')
    logo = Images.objects.get(name='logo')
    context={
        'products': products,
        'banner': banner,
        'banner1':ban_rgt_one,
        'banner2':ban_rgt_two,
        'banner3':ban_rgt_three,
        'banner4':ban_rgt_four,
        'logo':logo,
        
    }
    return render(request, 'base/index.html', context)

@login_required
def singleProduct(request,pk):
    product=Products.objects.get(id=pk)
    #room.message_set.all() permet de recuperer tout les messages poster dans la room
    
    context={
        'product':product,

       
    }
    return render(request,'base/single-product.html',context)

@login_required
def cart(request,pk):
    user = request.user
    product = Products.objects.get(id=pk)
    cart, _ = Cart.objects.get_or_create(user=user)# la methode get_or_create permet de recuperer un objet ou de de le creer s'il n'xiste pas. Cette methode renvoie deux valeur en premier l'objet et en second un autre parametre noté _ par convention 
    order, created = Order.objects.get_or_create(user=user, product=product)
    if created:
        cart.orders.add(order)
        cart.save()
    
    else:
        order.quantity +=1
        order.save()
    return redirect('base:single-product', pk=product.id)
    context={
        
    }
    return render(request,'base/cart.html', context)