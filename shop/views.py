from django.shortcuts import render,redirect, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.db.models import Q  # 3new
from shop.forms import ContactForm,UserRegisterForm

from django.core.paginator import InvalidPage, Paginator
from django.http import Http404


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    paginator = Paginator(products,16)
    is_paginated = True if paginator.num_pages > 1 else False
    page = request.GET.get('page') or 1
    try:
        current_page = paginator.page(page)
    except InvalidPage as e:
        raise Http404(str(e))

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'current_page': current_page,
        'is_paginated': is_paginated,
    }


    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()

    context = {
        'product': product,
        'cart_product_form': cart_product_form

    }



    return render(request, 'shop/product/detail.html', context)

def SearchRView(request):
    if not None:
        query = request.GET.get('q')
        pr = Product.objects.filter(Q(name__icontains=query) | Q(name__istartswith=query)| Q(name__endswith=query) | Q(name__istartswith=query)| Q(category__name__icontains=query)| Q(category__name__startswith=query)|Q(price__exact=query) | Q(image__icontains=query))
        # cr=Category.objects.filter(Q(name__icontains=query)|Q(name__iexact=query))


        return render(request, 'search/search_results.html', {'pr': pr})
    else:
        return redirect(product_detail)


# from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm
# from shop.form import u
from django.core.mail import EmailMessage
from django.template.loader import get_template

# from django.contrib.auth.models import User, Group
# from rest_framework import viewsets
# from .serializers import *

#
# # Create your views here.
#
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer


# redirect success page
def Success(request):
    return render(request, 'blog/success.html')


# sign up form
def SignUp(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect(Success)
    else:
        form = UserRegisterForm()
    return render(request, "registration/signup.html", {'form': form})


# Contact form view

def Contact(request):
    Contact_Form = ContactForm
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact_email')
            contact_content = request.POST.get('content')

            template = get_template('blog/contact_form.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_content': contact_content,
            }

            content = template.render(context)

            email = EmailMessage(
                "New contact form email",
                content,
                "Creative web" + '',
                ['myfriendkhendelwal@gmail.com'],
                headers={'Reply To': contact_email}
            )

            email.send()

            return redirect('blog:success')
    return render(request, 'blog/contact.html', {'form': Contact_Form})