from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages
from.models import *
from.forms import *


# Create your views here.


def accueil(request):
    products = Product.objects.order_by('-id')[:100]
    carousel = Photo.objects.all().order_by('-id')[:5]

    return render(request, 'commerce/accueil.html',
                  {'products': products,'carousel': carousel})



def display_product(request, product_id):
    """
    Cette fonction permet de visualiser un produit.
    :type request:
    :param request:
    :param product_id: Id du produit à visualiser
    :return:
    """

    product = get_object_or_404(Product, pk=product_id)
    pictures = Photo.objects.filter(product__pk=product.id)

    return render(request, 'commerce/product.html', {'product': product, 'pictures': pictures})

def commande(request,product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product_name': product.name,
        'product_id': product.id,
        'image': product.image,
    }
    if request.method == 'POST':
        form = ContactForm(request.POST, error_class=ParagraphErrorList)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            city = form.cleaned_data['city']
            quarter = form.cleaned_data['quarter']
            street=form.cleaned_data['street']
            door=form.cleaned_data['door']
            phone=form.cleaned_data['phone'] 

            try:
                    contact = Contact.objects.filter(email=email, name=name,
                            city=city,
                            quarter=quarter,
                            street=street,
                            door=door,
                            phone=phone)
                    if not contact.exists():
                        contact = Contact.objects.create(
                            email=email,
                            name=name,
                            city=city,
                            quarter=quarter,
                            street=street,
                            door=door,
                            phone=phone
                        )
                    else:
                        contact = contact.first()

                    product = get_object_or_404(Product, id=product_id)
                    order = Order.objects.create(
                        contact=contact,
                        product=product 
                    )
                    product.save()
                    return render(request,"commerce/merci.html",context)
            except:
                form.errors['internal'] = "Une erreur interne est apparue. Merci de recommencer votre requête."

    else:
        form = ContactForm()
    context['form'] = form
    context['errors'] = form.errors.items()
    return render(request, 'commerce/commande.html', context)




 
   

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product_name': product.name,
        'product_id': product.id,
        'image': product.image,
    }

    if request.method == 'POST':
        form = ContactForm(request.POST, error_class=ParagraphErrorList)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            city = form.cleaned_data['city']
            quarter = form.cleaned_data['quarter']
            street=form.cleaned_data['street']
            door=form.cleaned_data['door']
            phone=form.cleaned_data['phone'] 

            try:
                    contact = Contact.objects.filter(email=email)
                    if not contact.exists():
                        contact = Contact.objects.create(
                            email=email,
                            name=name,
                            city=city,
                            quarter=quarter,
                            street=street,
                            door=door,
                            phone=phone
                        )
                    else:
                        contact = contact.first()

                    product = get_object_or_404(Product, id=product_id)
                    order = Order.objects.create(
                        contact=contact,
                        product=product 
                    )
                    product.save()
                    return render(request, 'commerce/accueil.html', context)
            except:
                form.errors['internal'] = "Une erreur interne est apparue. Merci de recommencer votre requête."

    else:
        form = ContactForm()
    context['form'] = form
    context['errors'] = form.errors.items()
    return render(request, 'commerce/detail.html', context)







