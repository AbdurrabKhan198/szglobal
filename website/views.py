from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import (
    ContactEnquiry, 
    RiceProduct, 
    SpiceProduct, 
    PlywoodProduct, 
    IndustrialProduct, 
    SafetyShoeProduct
)


def home(request):
    """Homepage view with featured products"""
    context = {
        'rice_products': RiceProduct.objects.filter(is_active=True, is_featured=True)[:3],
        'spice_products': SpiceProduct.objects.filter(is_active=True, is_featured=True)[:3],
        'plywood_products': PlywoodProduct.objects.filter(is_active=True, is_featured=True)[:2],
        'industrial_products': IndustrialProduct.objects.filter(is_active=True, is_featured=True)[:4],
        'safety_products': SafetyShoeProduct.objects.filter(is_active=True, is_featured=True)[:4],
    }
    return render(request, 'website/index.html', context)


def rice(request):
    """Rice products page"""
    context = {
        'products': RiceProduct.objects.filter(is_active=True)
    }
    return render(request, 'website/products/rice.html', context)


def spices(request):
    """Spices products page"""
    context = {
        'products': SpiceProduct.objects.filter(is_active=True)
    }
    return render(request, 'website/products/spices.html', context)


def plywood(request):
    """Plywood products page"""
    context = {
        'products': PlywoodProduct.objects.filter(is_active=True)
    }
    return render(request, 'website/products/plywood.html', context)


def industrial(request):
    """Industrial items page"""
    context = {
        'products': IndustrialProduct.objects.filter(is_active=True)
    }
    return render(request, 'website/products/industrial.html', context)


def safety_shoes(request):
    """Safety shoes page"""
    context = {
        'products': SafetyShoeProduct.objects.filter(is_active=True)
    }
    return render(request, 'website/products/safety_shoes.html', context)


def all_products(request):
    """All products page showing all categories"""
    context = {
        'rice_products': RiceProduct.objects.filter(is_active=True)[:4],
        'spice_products': SpiceProduct.objects.filter(is_active=True)[:4],
        'plywood_products': PlywoodProduct.objects.filter(is_active=True)[:4],
        'industrial_products': IndustrialProduct.objects.filter(is_active=True)[:4],
        'safety_products': SafetyShoeProduct.objects.filter(is_active=True)[:4],
    }
    return render(request, 'website/all_products.html', context)


def about(request):
    """About page"""
    return render(request, 'website/about.html')


def contact(request):
    """Contact page with form"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            contact_obj = form.save()
            
            # Send email notification via Brevo
            try:
                from .email_service import send_contact_notification
                contact_data = {
                    'name': contact_obj.name,
                    'email': contact_obj.email,
                    'phone': contact_obj.phone or 'Not provided',
                    'subject': contact_obj.subject,
                    'message': contact_obj.message,
                }
                send_contact_notification(contact_data)
            except Exception as e:
                # Log error but don't break the flow
                print(f"Email notification failed: {e}")
            
            return redirect('website:thank_you')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    return render(request, 'website/contact.html', {'form': form})


def thank_you(request):
    """Thank you page after contact form submission"""
    return render(request, 'website/thank_you.html')
