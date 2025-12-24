from django.db import models
from django.utils import timezone


class ContactEnquiry(models.Model):
    """Contact Enquiries - Customer inquiries from contact form"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Enquiry'
        verbose_name_plural = 'Contact Enquiries'
    
    def __str__(self):
        return f"{self.name} - {self.subject} ({self.created_at.strftime('%Y-%m-%d')})"


class RiceProduct(models.Model):
    """Rice products that can be added via admin"""
    name = models.CharField(max_length=200, help_text="e.g., 1121 Golden Premium Sella Rice")
    description = models.TextField(help_text="Detailed product description")
    short_description = models.CharField(max_length=300, help_text="Brief description for cards")
    image_url = models.URLField(max_length=500, help_text="Paste image URL here")
    origin = models.CharField(max_length=100, default="India", help_text="e.g., Punjab & Haryana, India")
    grain_length = models.CharField(max_length=50, blank=True, help_text="e.g., 8.3mm+")
    features = models.TextField(help_text="Comma separated features, e.g., Long Grain, Aromatic, Non-Sticky")
    best_for = models.CharField(max_length=300, blank=True, help_text="e.g., Biryani, Pulao, Premium Dishes")
    is_featured = models.BooleanField(default=False, help_text="Show on homepage")
    is_active = models.BooleanField(default=True, help_text="Show on website")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower = first)")

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Rice Product'
        verbose_name_plural = 'Rice Products'

    def __str__(self):
        return self.name
    
    def get_features_list(self):
        return [f.strip() for f in self.features.split(',')]


class SpiceProduct(models.Model):
    """Spice products that can be added via admin"""
    name = models.CharField(max_length=200, help_text="e.g., Cinnamon (Dalchini)")
    description = models.TextField(help_text="Detailed product description")
    short_description = models.CharField(max_length=300, help_text="Brief description for cards")
    image_url = models.URLField(max_length=500, help_text="Paste image URL here")
    origin = models.CharField(max_length=100, default="India", help_text="e.g., Kerala, India")
    features = models.TextField(help_text="Comma separated features")
    uses = models.CharField(max_length=300, blank=True, help_text="e.g., Curries, Biryani, Garam Masala")
    is_featured = models.BooleanField(default=False, help_text="Show on homepage")
    is_active = models.BooleanField(default=True, help_text="Show on website")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower = first)")

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Spice Product'
        verbose_name_plural = 'Spice Products'

    def __str__(self):
        return self.name
    
    def get_features_list(self):
        return [f.strip() for f in self.features.split(',')]


class PlywoodProduct(models.Model):
    """Plywood products that can be added via admin"""
    name = models.CharField(max_length=200, help_text="e.g., 4x4 Feet Plywood Sheets")
    description = models.TextField(help_text="Detailed product description")
    short_description = models.CharField(max_length=300, help_text="Brief description for cards")
    image_url = models.URLField(max_length=500, help_text="Paste image URL here")
    size = models.CharField(max_length=100, blank=True, help_text="e.g., 4x4 Feet (1220x1220mm)")
    thickness = models.CharField(max_length=100, blank=True, help_text="e.g., 6mm to 25mm")
    grade = models.CharField(max_length=100, blank=True, help_text="e.g., BWR, BWP, MR")
    features = models.TextField(help_text="Comma separated features")
    applications = models.CharField(max_length=300, blank=True, help_text="e.g., Furniture, Construction")
    is_featured = models.BooleanField(default=False, help_text="Show on homepage")
    is_active = models.BooleanField(default=True, help_text="Show on website")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower = first)")

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Plywood Product'
        verbose_name_plural = 'Plywood Products'

    def __str__(self):
        return self.name
    
    def get_features_list(self):
        return [f.strip() for f in self.features.split(',')]


class IndustrialProduct(models.Model):
    """Industrial products that can be added via admin"""
    CATEGORY_CHOICES = [
        ('manufacturing', 'Manufacturing Machinery'),
        ('construction', 'Construction Equipment'),
        ('power_tools', 'Power Tools'),
        ('material_handling', 'Material Handling'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=200, help_text="e.g., CNC Machine")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    description = models.TextField(help_text="Detailed product description")
    short_description = models.CharField(max_length=300, help_text="Brief description for cards")
    image_url = models.URLField(max_length=500, help_text="Paste image URL here")
    features = models.TextField(help_text="Comma separated features")
    specifications = models.TextField(blank=True, help_text="Technical specifications")
    is_featured = models.BooleanField(default=False, help_text="Show on homepage")
    is_active = models.BooleanField(default=True, help_text="Show on website")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower = first)")

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Industrial Product'
        verbose_name_plural = 'Industrial Products'

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"
    
    def get_features_list(self):
        return [f.strip() for f in self.features.split(',')]


class SafetyShoeProduct(models.Model):
    """Safety Shoes products that can be added via admin"""
    SHOE_TYPE_CHOICES = [
        ('steel_toe', 'Steel Toe Boots'),
        ('low_cut', 'Low-Cut Safety Shoes'),
        ('composite', 'Composite Toe Shoes'),
        ('waterproof', 'Waterproof Boots'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=200, help_text="e.g., Steel Toe Safety Boots")
    shoe_type = models.CharField(max_length=50, choices=SHOE_TYPE_CHOICES, default='steel_toe')
    description = models.TextField(help_text="Detailed product description")
    short_description = models.CharField(max_length=300, help_text="Brief description for cards")
    image_url = models.URLField(max_length=500, help_text="Paste image URL here")
    features = models.TextField(help_text="Comma separated features")
    sizes_available = models.CharField(max_length=100, blank=True, help_text="e.g., UK 5-13")
    certifications = models.CharField(max_length=200, blank=True, help_text="e.g., EN ISO 20345, ASTM F2413")
    best_for = models.CharField(max_length=300, blank=True, help_text="e.g., Construction, Manufacturing")
    is_featured = models.BooleanField(default=False, help_text="Show on homepage")
    is_active = models.BooleanField(default=True, help_text="Show on website")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower = first)")

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Safety Shoe Product'
        verbose_name_plural = 'Safety Shoe Products'

    def __str__(self):
        return f"{self.name} ({self.get_shoe_type_display()})"
    
    def get_features_list(self):
        return [f.strip() for f in self.features.split(',')]


# Keep old Contact model for backward compatibility (alias)
Contact = ContactEnquiry
