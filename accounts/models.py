# from django.db import models


import datetime
from typing import AbstractSet
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

# class CustomUser(AbstractBaseUser):
#     username = models.CharField(max_length=255, unique=True)
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     # Additional fields
#     phone = models.CharField(max_length=20, blank=True, null=True)
#     address = models.CharField(max_length=255, blank=True, null=True)
#     # Add other fields...

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']

#     def __str__(self):
#         return self.username
    

class CustomUser(AbstractUser):
    # Additional fields
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(
        max_length=10, 
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        blank=True, null=True
    )
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    emergency_contact = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    # You can also define the user manager if needed (below).

    def __str__(self):
        return self.username
    



    def has_perm(self, perm, obj=None):
        """
        Returns True if the user has the given permission. This is used by Django 
        to check permissions for the user.
        """
        # Admins or superusers always have all permissions
        if self.is_superuser:
            return True
        
        # You can customize this further if needed, for example, by checking the user's
        # permissions based on some group or permission model.
        return self.user_permissions.filter(codename=perm).exists()

    def has_module_perms(self, app_label):
        """
        Returns True if the user has permissions for the given app label.
        """
        if self.is_superuser:
            return True
        # You can check app-level permissions based on your app structure or groups
        return self.user_permissions.filter(content_type__app_label=app_label).exists()




class Destination(models.Model):

    name =  models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)





# class Tour(models.Model):
#     # Define a choice field for international or domestic
#     TOUR_TYPE_CHOICES = [
#         ('domestic', 'Domestic'),
#         ('international', 'International'),
#     ]
    
#     # Basic Tour Details
#     tour_name = models.CharField(max_length=100)
#     description = models.TextField(
#     null=True,
#     blank=True,
#     help_text="Enter description."
#     )
#     description1 = models.TextField(
#     null=True,
#     blank=True,
#     help_text="Enter description1."
#     )
#     description2 = models.TextField(
#     null=True,
#     blank=True,
#     help_text="Enter description2."
#     )
#     # description = models.TextField()
#     duration = models.IntegerField()  # Duration in days
#     price_per_person = models.DecimalField(max_digits=10, decimal_places=2)
#     deluxe_price_per_person = models.DecimalField(max_digits=10, decimal_places=2)
#     super_deluxe_price_per_person = models.DecimalField(max_digits=10, decimal_places=2)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     accommodation = models.CharField(max_length=255, null=True, blank=True)  # Accommodation details
#     transportation = models.CharField(max_length=255, null=True, blank=True)  # Transportation details
#     meals = models.TextField(null=True, blank=True)  # Meals included (optional)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Total price for the package
#     available = models.BooleanField(default=True)  # Availability of the package
#     discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Optional discount
#     image = models.ImageField(upload_to='package_images/', null=True, blank=True)  # Image for the package

#     # Tour Type Field
#     tour_type = models.CharField(
#         max_length=13,  # Increased max_length to accommodate 'international'
#         choices=TOUR_TYPE_CHOICES,
#         default='domestic',  # Default to 'domestic' if not specified
#     )
    
#     # Fields for included and not-included items
#     include = models.TextField(
#         null=True,
#         blank=True,
#         help_text="Enter items included in the tour, separated by commas or new lines."
#     )
#     not_include = models.TextField(
#         null=True,
#         blank=True,
#         help_text="Enter items not included in the tour, separated by commas or new lines."
#     )
#     table_of_content = models.TextField(
#         null=True,
#         blank=True,
#         help_text="Enter items not table_of_content in the tour, separated by commas or new lines."
#     )
#     summary = models.TextField(
#         null=True,
#         blank=True,
#         help_text="Enter items not summary in the tour, separated by commas or new lines."
#     )
#     deluxe  = models.TextField(
#         null=True,
#         blank=True,
#         help_text="Enter items not deluxe in the tour, separated by commas or new lines."
#     )
#     super_deluxe = models.TextField(
#         null=True,
#         blank=True,
#         help_text="Enter items not super_deluxe in the tour, separated by commas or new lines."
#     )
#     user = models.ForeignKey(
#         get_user_model(),  # This will get the user model (CustomUser)
#         on_delete=models.SET_NULL,  # Set to null if the user is deleted
#         null=True,  # Allow null for when no user is assigned
#         blank=True,  # Allow it to be optional
#     )

#     def __str__(self):
#         return self.tour_name
    
    

#     def calculate_discounted_price(self):
#         """
#         Calculate the discounted price based on the total price and discount.
#         """
#         if self.discount:
#             return self.total_price * (1 - (self.discount / 100))
#         return self.total_price


class Tour(models.Model):
    # Define a choice field for international or domestic
    TOUR_TYPE_CHOICES = [
        ('domestic', 'Domestic'),
        ('international', 'International'),
    ]
    
    # Basic Tour Details
    tour_name = models.CharField(max_length=100)
    tour_title_details = models.CharField(max_length=200, null=True,blank=True)
    description = models.TextField(
        null=True,
        blank=True,
        help_text="General tour description."
    )
    description1 = models.TextField(
        null=True,
        blank=True,
        help_text="General tour description1."
    )
    description2 = models.TextField(
        null=True,
        blank=True,
        help_text="General tour description2."
    )
    duration = models.IntegerField(null=True,blank=True)  # Duration in days
    # price_per_person = models.DecimalField(max_digits=10, decimal_places=2)
    deluxe_price_per_person = models.IntegerField(null=True,blank=True)
    super_deluxe_price_per_person = models.IntegerField(null=True,blank=True)
    start_date = models.DateField()  # or models.DateTimeField()
    end_date = models.DateField()    # or models.DateTimeField()
    # accommodation = models.CharField(max_length=255, null=True, blank=True)  # Accommodation details
    # transportation = models.CharField(max_length=255, null=True, blank=True)  # Transportation details
    # meals = models.TextField(null=True, blank=True)  # Meals included (optional)
    total_night = models.IntegerField(null=True,blank=True)  # Total price for the package
    total_days = models.IntegerField(null=True,blank=True)  # Total price for the package
    available = models.BooleanField(default=True, null=True,blank=True)  # Availability of the package
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Optional discount
    image = models.ImageField(upload_to='package_images/', null=True, blank=True)  # Image for the package
    summary_image = models.ImageField(upload_to='summary_images/', null=True, blank=True)  # Image for the package

    # Tour Type Field
    tour_type = models.CharField(
        max_length=13,
        choices=TOUR_TYPE_CHOICES,
        default='domestic',null=True,blank=True,
    )
    
    # Fields for included and not-included items
    include = models.TextField(
        null=True,
        blank=True,
        help_text="Enter items included in the tour, separated by commas or new lines."
    )
    not_include = models.TextField(
        null=True,
        blank=True,
        help_text="Enter items not included in the tour, separated by commas or new lines."
    )
    table_of_content = models.TextField(
        null=True,
        blank=True,
        help_text="Enter items for the table of contents, separated by commas or new lines."
    )
    summary = models.TextField(
        null=True,
        blank=True,
        help_text="Enter a summary of the tour."
    )
    deluxe = models.TextField(
        null=True,
        blank=True,
        help_text="Enter deluxe details of the tour."
    )
    super_deluxe = models.TextField(
        null=True,
        blank=True,
        help_text="Enter super deluxe details of the tour."
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.tour_name

    def calculate_discounted_price(self):
        """
        Calculate the discounted price based on the total price and discount.
        """
        if self.discount:
            return self.total_price * (1 - (self.discount / 100))
        return self.total_price


class TourDay(models.Model):
    """
    Model to represent the details of each day of the tour.
    """
    
    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name="days"
    )
    day_wise_plan = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.tour.tour_name
    

class Tourist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Link to the logged-in user
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    passport_number = models.CharField(max_length=20, null=True, blank=True)
    nationality = models.CharField(max_length=50)
    number_of_people = models.PositiveIntegerField(default=1)  # Default to 1
    payment_status = models.CharField(max_length=20, default='Pending')
    special_request = models.TextField(null=True, blank=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='tourists')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Link to the logged-in user
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    BOOKING_STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('pending', 'Pending'),
    ]

    tourist = models.ForeignKey('Tourist', on_delete=models.CASCADE, related_name='bookings')
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE, related_name='bookings')
    number_of_people = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=10,
        choices=PAYMENT_STATUS_CHOICES,
        default='pending',
    )
    booking_status = models.CharField(
        max_length=10,
        choices=BOOKING_STATUS_CHOICES,
        default='pending',
    )

    def __str__(self):
        return f"Booking for {self.tourist} on {self.tour}"