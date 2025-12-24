from django.contrib import admin
from .models import (
    ContactEnquiry, 
    RiceProduct, 
    SpiceProduct, 
    PlywoodProduct, 
    IndustrialProduct, 
    SafetyShoeProduct
)


@admin.register(ContactEnquiry)
class ContactEnquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']
    list_editable = ['is_read']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Message', {
            'fields': ('subject', 'message')
        }),
        ('Status', {
            'fields': ('is_read', 'created_at')
        }),
    )


@admin.register(RiceProduct)
class RiceProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'origin', 'is_featured', 'is_active', 'order', 'created_at']
    list_filter = ['is_featured', 'is_active', 'origin']
    search_fields = ['name', 'description']
    list_editable = ['is_featured', 'is_active', 'order']
    ordering = ['order', '-created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'short_description', 'description')
        }),
        ('Image', {
            'fields': ('image_url',),
            'description': 'Paste the full image URL (e.g., from Unsplash or your CDN)'
        }),
        ('Product Details', {
            'fields': ('origin', 'grain_length', 'features', 'best_for')
        }),
        ('Display Settings', {
            'fields': ('is_featured', 'is_active', 'order')
        }),
    )


@admin.register(SpiceProduct)
class SpiceProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'origin', 'is_featured', 'is_active', 'order', 'created_at']
    list_filter = ['is_featured', 'is_active', 'origin']
    search_fields = ['name', 'description']
    list_editable = ['is_featured', 'is_active', 'order']
    ordering = ['order', '-created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'short_description', 'description')
        }),
        ('Image', {
            'fields': ('image_url',),
            'description': 'Paste the full image URL'
        }),
        ('Product Details', {
            'fields': ('origin', 'features', 'uses')
        }),
        ('Display Settings', {
            'fields': ('is_featured', 'is_active', 'order')
        }),
    )


@admin.register(PlywoodProduct)
class PlywoodProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'size', 'thickness', 'is_featured', 'is_active', 'order']
    list_filter = ['is_featured', 'is_active', 'grade']
    search_fields = ['name', 'description']
    list_editable = ['is_featured', 'is_active', 'order']
    ordering = ['order', '-created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'short_description', 'description')
        }),
        ('Image', {
            'fields': ('image_url',),
        }),
        ('Specifications', {
            'fields': ('size', 'thickness', 'grade', 'features', 'applications')
        }),
        ('Display Settings', {
            'fields': ('is_featured', 'is_active', 'order')
        }),
    )


@admin.register(IndustrialProduct)
class IndustrialProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'is_featured', 'is_active', 'order', 'created_at']
    list_filter = ['category', 'is_featured', 'is_active']
    search_fields = ['name', 'description']
    list_editable = ['is_featured', 'is_active', 'order']
    ordering = ['order', '-created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'short_description', 'description')
        }),
        ('Image', {
            'fields': ('image_url',),
        }),
        ('Product Details', {
            'fields': ('features', 'specifications')
        }),
        ('Display Settings', {
            'fields': ('is_featured', 'is_active', 'order')
        }),
    )


@admin.register(SafetyShoeProduct)
class SafetyShoeProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'shoe_type', 'sizes_available', 'is_featured', 'is_active', 'order']
    list_filter = ['shoe_type', 'is_featured', 'is_active']
    search_fields = ['name', 'description']
    list_editable = ['is_featured', 'is_active', 'order']
    ordering = ['order', '-created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'shoe_type', 'short_description', 'description')
        }),
        ('Image', {
            'fields': ('image_url',),
        }),
        ('Product Details', {
            'fields': ('features', 'sizes_available', 'certifications', 'best_for')
        }),
        ('Display Settings', {
            'fields': ('is_featured', 'is_active', 'order')
        }),
    )


# Customize admin site header
admin.site.site_header = "SZ Global Arabia Traders - Admin"
admin.site.site_title = "SZ Global Admin"
admin.site.index_title = "Manage Your Products & Enquiries"
