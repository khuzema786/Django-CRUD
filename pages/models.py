from django.db import models

# Create your models here.
class Form(models.Model):
    industry_choices = (
        ('Restaurents and Bars', 'Restaurents and Bars'),
        ('Event Ticketing and Management', 'Event Ticketing and Management'),
        ('Travel - Airline/Hotel/Cruise/Rentals', 'Travel - Airline/Hotel/Cruise/Rentals'),
        ('Commericial Real Estate/Building Management', 'Commericial Real Estate/Building Management'),
        ('Movie Theaters', 'Movie Theaters'),
        ('Sports/Concerts/Event Venues', 'Sports/Concerts/Event Venues'),
        ('Schools and Colleges', 'Schools and Colleges'),
        ('Place of Worship', 'Place of Worship'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Government organizations', 'Government organizations'),
    )
    designation_choices = (
        ('Individual', 'Individual'),
        ('Buisness', 'Buisness'),
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    designation = models.CharField(choices=designation_choices, max_length=255)    
    industry = models.CharField(choices=industry_choices, max_length=100)
    website = models.URLField(max_length=100, blank=True)
    description = models.TextField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)