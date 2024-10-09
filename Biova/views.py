from django.shortcuts import render
from .models import Product, Categorie, Review, Blog
from django.core.paginator import Paginator 
from django.views.generic import DetailView


def index(request):
    products = Product.objects.all()
    category = Categorie.objects.all()
    review = Review.objects.all()
    blog = Blog.objects.all()
    
    item_name = request.GET.get("item_name", "")
    
    if item_name:
        products = products.filter(name__icontains=item_name)
    
    
   #paginator code
    paginator = Paginator(products, 3)
    page =  request.GET.get("page")
    products = paginator.get_page(page)
    
    
    context = {
        "products": products, 
        "category": category, 
        "review": review,
        "blog": blog,
    }
    
    return render(request, "Biova/index.html", context)
    
    
    
    
    
    
class ProductDetailView(DetailView):
    model = Product
    fields = "__all__"


class BlogDetailView(DetailView):
    model = Blog
    fields = "__all__"