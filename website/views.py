from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Contact

def home(request):
    """Homepage view"""
    return render(request, 'website/index.html')

def rice(request):
    """Rice products page"""
    return render(request, 'website/products/rice.html')

def spices(request):
    """Spices products page"""
    return render(request, 'website/products/spices.html')

def plywood(request):
    """Plywood products page"""
    return render(request, 'website/products/plywood.html')

def industrial(request):
    """Industrial items page"""
    return render(request, 'website/products/industrial.html')

def safety_shoes(request):
    """Safety shoes page"""
    return render(request, 'website/products/safety_shoes.html')

def all_products(request):
    """All products page showing all categories"""
    return render(request, 'website/all_products.html')

def about(request):
    """About page"""
    return render(request, 'website/about.html')

def contact(request):
    """Contact page with form"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
            return redirect('website:contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    return render(request, 'website/contact.html', {'form': form})
