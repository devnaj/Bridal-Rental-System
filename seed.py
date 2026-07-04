import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bridalsystem.settings')
django.setup()

from rentals.models import Category, Product, Booking

def seed_db():
    print("Clearing old data...")
    Booking.objects.all().delete()
    Product.objects.all().delete()
    Category.objects.all().delete()
    
    print("Creating Categories...")
    lehenga_cat = Category.objects.create(name="Bridal Lehengas")
    jewelry_cat = Category.objects.create(name="Temple Jewelry")
    saree_cat = Category.objects.create(name="Silk Sarees")
    
    print("Creating Products...")
    products = [
        # Lehengas
        Product(name="Crimson Zari Royal Lehenga", category=lehenga_cat, description="A completely hand-embroidered deep red silk lehenga featuring pure gold Zardosi work. Worn by royalty, preserved for sustainability. Includes matching dupatta.", image="bridal_inventory/lehenga.jpg", rental_price=12000, security_deposit=25000, status="available", water_saved=3200, carbon_offset=45.5),
        Product(name="Ivory Sequence Reception Gown", category=lehenga_cat, description="Contemporary ivory bridal gown with intricate silver sequin work. Perfect for evening receptions and modern sustainable brides.", image="bridal_inventory/lehenga_2.jpg", rental_price=8500, security_deposit=15000, status="available", water_saved=2100, carbon_offset=30.0),
        Product(name="Emerald Heritage Velvet Lehenga", category=lehenga_cat, description="Rich emerald green velvet lehenga with antique gold embroidery. Heavy flare with dual dupattas.", image="bridal_inventory/lehenga_3.jpg", rental_price=15000, security_deposit=30000, status="available", water_saved=4500, carbon_offset=60.2),
        Product(name="Blush Pink Floral Organza", category=lehenga_cat, description="Lightweight pastel pink organza lehenga with 3D floral appliqués. Perfect for daytime wedding events.", image="bridal_inventory/lehenga_4.jpg", rental_price=6500, security_deposit=12000, status="available", water_saved=1800, carbon_offset=22.5),
        Product(name="Midnight Blue Sangeet Special", category=lehenga_cat, description="Deep navy blue georgette lehenga with mirror work. Incredible twirl factor for sangeet performances.", image="bridal_inventory/lehenga_5.jpg", rental_price=7000, security_deposit=14000, status="available", water_saved=2000, carbon_offset=28.0),
        
        # Jewelry
        Product(name="Antique Gold Kundan Choker Base", category=jewelry_cat, description="Heavy 22k gold-plated authentic Kundan choker necklace with matching oversized earrings and maang tikka.", image="bridal_inventory/jewelry.jpg", rental_price=4500, security_deposit=10000, status="available", water_saved=500, carbon_offset=12.5),
        Product(name="South Indian Temple Haar", category=jewelry_cat, description="Long traditional temple jewelry necklace featuring Goddess Lakshmi motifs and ruby droplets.", image="bridal_inventory/jewelry_2.jpg", rental_price=3500, security_deposit=8000, status="available", water_saved=400, carbon_offset=10.0),
        Product(name="Polki Bridal Set with Emeralds", category=jewelry_cat, description="Stunning uncut diamond (Polki) imitation set paired with large emerald beads. Includes matha patti.", image="bridal_inventory/jewelry_3.jpg", rental_price=6000, security_deposit=15000, status="available", water_saved=600, carbon_offset=15.0),
        Product(name="Jadau Rajwadi Bridal Chura", category=jewelry_cat, description="Complete traditional bridal bangle set with intricate Jadau work and kundan accents.", image="bridal_inventory/jewelry_4.jpg", rental_price=2000, security_deposit=5000, status="available", water_saved=200, carbon_offset=5.0),
        Product(name="Nizam Pearl Satlada", category=jewelry_cat, description="Seven-tier pearl necklace with small Polki pendants. Classic Nawabi elegance.", image="bridal_inventory/jewelry_5.jpg", rental_price=3000, security_deposit=7000, status="available", water_saved=300, carbon_offset=8.0),
    ]
    
    Product.objects.bulk_create(products)
    print("Database seeded completely!")

if __name__ == '__main__':
    seed_db()
