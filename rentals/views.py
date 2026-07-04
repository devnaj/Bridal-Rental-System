from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Category, Booking
from .forms import BookingForm

def catalog(request):
    """Displays bridal items with status 'Available'."""
    products = Product.objects.filter(status='available')
    categories = Category.objects.all()
    
    query = request.GET.get('q')
    if query:
        products = products.filter(name__icontains=query) | products.filter(description__icontains=query)
        
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)
        
    return render(request, 'rentals/catalog.html', {'products': products, 'categories': categories})

# FIXED: Added this function to resolve the AttributeError
def product_detail(request, pk):
    """Displays detailed info for a specific bridal item."""
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'rentals/product_detail.html', {'product': product})

@login_required
def book_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        form.instance.user = request.user
        form.instance.product = product
        if form.is_valid():
            form.save()
            product.status = 'rented'
            product.save()
            messages.success(request, f"Successfully reserved {product.name}!")
            return redirect('user_dashboard')
    else:
        form = BookingForm()
    return render(request, 'rentals/booking_form.html', {'form': form, 'product': product})

@login_required
def user_dashboard(request):
    """Calculates impact using 'water_saved' and 'carbon_offset' fields."""
    user_bookings = Booking.objects.filter(user=request.user).select_related('product')
    total_water = user_bookings.aggregate(Sum('product__water_saved'))['product__water_saved__sum'] or 0
    total_impact = user_bookings.aggregate(Sum('product__carbon_offset'))['product__carbon_offset__sum'] or 0
    
    return render(request, 'rentals/dashboard.html', {
        'bookings': user_bookings,
        'total_water': total_water,
        'total_waste': total_impact
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created! Please log in.")
            return redirect('login')
    else:
        form = UserCreationForm()
    # Points to the 'registration' subfolder seen in your explorer
    return render(request, 'rentals/registration/register.html', {'form': form})