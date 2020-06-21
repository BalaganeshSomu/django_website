from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Post,Contact,About,Product
from django.views.generic import (ListView)
# Create your views here.

def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'home/home.html',context)

class PostListView(ListView):
    model=Post
    template_name='home/home.html' 
    context_object_name='posts'
    ordering=['-date_posted']

def about(request):
    context={
        'abouts':About.objects.all()
    }
    return render(request,'home/about.html',context)

def contact(request):
    context={
        'contacts':Contact.objects.all()
    }
    return render(request,'home/contact.html',context)

def product(request):
    context={
        'products':Product.objects.all()
    }
    return render(request,'home/product.html',context)