from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.models import Group, User
from .forms import SignUpForm

# Create your views here.
def index(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {"categories":categories})

def allProducts(request, c_slug=None):
    c_page = None
    products_list = None
    if c_slug!=None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.filter(category=c_page, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)
        # Pagination Code
    paginator = Paginator(products_list, 6)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        product = paginator.page(paginator.num_pages)
    return render(request, 'category.html', {'category':c_page, 'products':products})


def productDetailPage(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html',{"product":product})
