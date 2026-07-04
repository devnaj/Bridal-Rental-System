from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta: verbose_name_plural = "Categories"
    def __str__(self): return self.name

class Product(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('cleaning', 'Cleaning/Maintenance'),
    ]
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='bridal_inventory/')
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    
    # SDG 12 Metrics
    water_saved = models.IntegerField(help_text="Liters of water saved by renting")
    carbon_offset = models.DecimalField(max_digits=5, decimal_places=2, help_text="kg of CO2 offset")

    def __str__(self): return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def clean(self):
        if not self.start_date or not self.end_date:
            return
            
        # Prevent overlapping bookings
        overlap = Booking.objects.filter(
            product=self.product,
            start_date__lt=self.end_date,
            end_date__gt=self.start_date
        ).exists()
        if overlap:
            raise ValidationError(f"This item is already booked for the selected dates.")
        if self.start_date < timezone.now().date():
            raise ValidationError("Booking cannot be in the past.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
