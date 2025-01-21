import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Booking, CustomUser, Destination, TourDay, Tourist
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Tour, Tour    # Import the models
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# Create your views here.
import re
from django.shortcuts import get_object_or_404, render
from .models import Tour, TourDay

def index(request):

    dests = Destination.objects.all()

    Tours = Tour.objects.all()[:4]
    international_tours = Tour.objects.filter(tour_type='International').order_by('id')[:9]
    domestic_tours = Tour.objects.filter(tour_type='Domestic').order_by('id')[:9]

    d = {'Tours':Tours,'dests':dests,'international_tours':international_tours,'domestic_tours':domestic_tours}

    return render(request, 'index.html', d)

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(username=username, password=password)

#         if user is not None:
#             auth.login(request, user)
#             return redirect('/')
#         else:
#             messages.info(request, 'invalid credentials...')
#             return redirect('login')
#     else:
#         return render(request, 'login.html')

# def register(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']

#         if password1==password2:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, "username taken...")
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request, "email taken...")
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
#                 user.save()
#                 messages.info(request, "user created...")
#                 return redirect('login')
#         else:
#             messages.info(request, "password not matched...")
#             return redirect('register')
#         return redirect('/')
#     else:
#         return render(request, 'register.html')


def signup(request):
    if request.method == 'POST':
        # Collect form data
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        phone = request.POST['phone']
        address = request.POST['address']
        country = request.POST['country']  # Fix typo from 'cuntry'
        state = request.POST['state']
        city = request.POST['city']
        gender = request.POST['gender']
        postal_code = request.POST['postal_code']
        emergency_contact = request.POST['emergency_contact']
        image = request.FILES.get('image')  # Image for the profile
        
        # Check if passwords match
        if password1 == password2:
            # Ensure the username and email are unique
            if CustomUser.objects.filter(username=username).exists():
                messages.info(request, "Username taken...")
                return redirect('signup.html')
            elif CustomUser.objects.filter(email=email).exists():
                messages.info(request, "Email taken...")
                return redirect('signup.html')
            else:
                # Create the user using CustomUser
                user_profile = CustomUser.objects.create_user(
                    username=username,
                    password=password1,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    phone=phone,
                    address=address,
                    country=country,
                    state=state,
                    city=city,
                    gender=gender,
                    postal_code=postal_code,
                    emergency_contact=emergency_contact,
                    image=image  # Save the image field
                )
                user_profile.save()

                messages.info(request, "User created successfully")
                return redirect('signin')  # Redirect to login page after successful signup
        else:
            messages.info(request, "Passwords do not match...")
            return redirect('register')  # If passwords don't match, redirect back to the signup page
    else:
        return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def news(request):
    return render(request, 'news.html')

def destinations(request):
    return render(request, 'destinations.html')


def package(request):
    return render(request, 'package.html')

def service(request):
    return render(request, 'service.html')

def International_packages(request):
    Tours = Tour.objects.filter(tour_type='international')
    return render(request, 'International_packages.html',{'Tours':Tours})

def Domestic_packges(request):
    Tours = Tour.objects.filter(tour_type='domestic')
    return render(request, 'Domestic_packges.html',{'Tours':Tours})



# def package_details(request, id):
#     # Fetch the package object based on the ID
#     details = get_object_or_404(Tour, id=id)
#     Tours = Tour.objects.all()[:4]
#     image = Tour.objects.filter(id=id).values_list('image', flat=True).first()
#     tour_name_before_package = details.tour_name.split("Package")[0].strip()
#     # Process 'include' field
#     raw_data = Tour.objects.filter(id=id).values_list('include', flat=True).first()
#     formatted_data = raw_data.replace('\r\n\r\n', '\n') if raw_data else None
    
#     # Process 'not_include' field
#     raw_data1 = Tour.objects.filter(id=id).values_list('not_include', flat=True).first()
#     formatted_data1 = raw_data1.replace('\r\n\r\n', '\n') if raw_data1 else None

#     raw_data2 = Tour.objects.filter(id=id).values_list('description', flat=True).first()
#     formatted_data2 = raw_data2.replace('\r\n\r\n', '\n') if raw_data2 else None

#     description1_raw_data2 = Tour.objects.filter(id=id).values_list('description1', flat=True).first()
#     description_formatted_data1 = description1_raw_data2.replace('\r\n\r\n', '\n') if description1_raw_data2 else None

#     description2_raw_data2 = Tour.objects.filter(id=id).values_list('description2', flat=True).first()
#     description_formatted_data2 = description2_raw_data2.replace('\r\n\r\n', '\n') if description2_raw_data2 else None

#     raw_data3 = Tour.objects.filter(id=id).values_list('table_of_content', flat=True).first()
#     formatted_data3 = raw_data3.replace('\r\n\r\n', '\n') if raw_data3 else None
    
#     raw_data4 = Tour.objects.filter(id=id).values_list('summary', flat=True).first()
#     formatted_data4 = raw_data4.replace('\r\n\r\n', '\n') if raw_data4 else None

#     deluxe = Tour.objects.filter(id=id).values_list('deluxe', flat=True).first()
#     formatted_data5 = deluxe.replace('\r\n\r\n', '\n') if deluxe else None

#     super_deluxe = Tour.objects.filter(id=id).values_list('super_deluxe', flat=True).first()
#     formatted_data6 = super_deluxe.replace('\r\n\r\n', '\n') if super_deluxe else None

#     # Pass details, include, and not_include to the template
#     return render(request, 'package_details.html', {
#         'image':image,
#         'Tours':Tours,
#         'details': details,
#         'tour_name_before_package':tour_name_before_package,
#         'include': formatted_data,
#         'not_include': formatted_data1,
#         'description': formatted_data2,
#         'description1': description_formatted_data1,
#         'description2': description_formatted_data2,
#         'table_of_content': formatted_data3,
#         'summary': formatted_data4,
#         'deluxe': formatted_data5,
#         'super_deluxe': formatted_data6,
#     })
@login_required(login_url='signin') 
def package_details(request, id):
    # Fetch the package object based on the ID
    details = get_object_or_404(Tour, id=id)
    # days_details = get_object_or_404(TourDay, id=id)
    days_details = TourDay.objects.filter(tour_id=id).order_by('id')
    for day in days_details:
        # Split the description by 3 or more consecutive spaces
        day.description_split = re.split(r'\s{3,}', day.description)
    tour = Tour.objects.filter(id=id).first()

    # Check if tour exists to avoid errors
    if tour:
        total_night = tour.total_night
        total_days = tour.total_days

        # Extract start and end dates
        start_date = tour.start_date
        end_date = tour.end_date
        
        # Extract months from start_date and end_date
        start_month = start_date.strftime('%B')  # '%B' gives the full month name (e.g., April)
        end_month = end_date.strftime('%B')      # '%B' gives the full month name (e.g., May)

    else:
        total_night = total_days = start_month = end_month = None  # Handle case where no such tour exists


    Tours = Tour.objects.all()
    tours_international = Tour.objects.filter(tour_type='international')
    tours_domestic = Tour.objects.filter(tour_type='domestic')
    image = details.image
    tour_name_before_package = details.tour_name.split("Package")[0].strip()
        # Calculate days and nights
    if details.start_date and details.end_date:
        duration = (details.end_date - details.start_date).days
        nights = max(0, duration - 1)  # At least 0 nights
    else:
        duration = nights = None

    # Process fields like 'include', 'not_include', etc.
    def process_raw_data(field):
        raw_data = getattr(details, field, None)
        return raw_data.replace('\r\n\r\n', '\n') if raw_data else None

    formatted_data = process_raw_data('include')
    formatted_data1 = process_raw_data('not_include')
    formatted_data2 = process_raw_data('description')
    description_formatted_data1 = process_raw_data('description1')
    description_formatted_data2 = process_raw_data('description2')
    formatted_data3 = process_raw_data('table_of_content')
    formatted_data4 = process_raw_data('summary')
    formatted_data5 = process_raw_data('deluxe')
    formatted_data6 = process_raw_data('super_deluxe')

    # Handle tourist form submission
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        passport_number = request.POST.get('passport_number')
        nationality = request.POST.get('nationality')
        number_of_people = request.POST.get('number_of_people')
        total_amount = request.POST.get('total_amount')

        # Set default values for payment and booking status
        payment_status = "Pending"
        booking_status = "Pending"

        # Check if the user is logged in and associate the user ID
        if request.user.is_authenticated:
            user = request.user
        else:
            # You can redirect or show an error if the user is not logged in
            messages.error(request, "You need to be logged in to make a booking.")
            return redirect('login')  # Assuming you have a 'login' URL

        # Save the tourist data and associate it with the selected tour
        tourist = Tourist.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            number_of_people=number_of_people,
            tour=details,  # Assign the Tour object to the tourist
            user=user  # Associate the logged-in user
        )

        # Ensure the 'tour' is being passed correctly to the Booking creation
        if details:
            Booking.objects.create(
                tourist=tourist,
                tour=details,  # Pass the 'details' object correctly here
                number_of_people=number_of_people,
                total_amount=int(total_amount) * int(number_of_people),
                payment_status=payment_status,
                booking_status=booking_status,
                user=user  # Associate the user with the booking
            )

        # After saving the data, add a success message and redirect
        messages.success(request, "Your booking has been successfully submitted!")
        
        return redirect('package_details', id=id)

    # Fetch tourists associated with the package
    tourists = details.tourists.all()

    # Pass all necessary context data to the template
    return render(request, 'package_details.html', {
        'image': image,
        'Tours': Tours,
        'tours_international':tours_international,
        'tours_domestic':tours_domestic,
        'total_night':total_night,
        'total_days':total_days,
        'start_month':start_month,
        'end_month':end_month,
        'details': details,
        'days_details': days_details,
        'duration': duration,
         'nights': nights,
        'tour_name_before_package': tour_name_before_package,
        'include': formatted_data,
        'not_include': formatted_data1,
        'description': formatted_data2,
        'description1': description_formatted_data1,
        'description2': description_formatted_data2,
        'table_of_content': formatted_data3,
        'summary': formatted_data4,
        'deluxe': formatted_data5,
        'super_deluxe': formatted_data6,
        'tourists': tourists,
    })
@csrf_exempt
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            # Add a success message
            # messages.success(request, 'Login successful!')
            return redirect('/')
        else:
            # Add an error message for invalid credentials
            # messages.error(request, 'Invalid credentials. Please try again.')
            return redirect('signin')
    else:
        return render(request, 'signin.html')
    
def my_booking(request):
    user = request.user  # Get the logged-in user
    user_id = request.user.id  # Get the logged-in user

    # Retrieve all Tourist entries associated with the logged-in user
    tourists = Tourist.objects.filter(user_id=user_id)

    # Retrieve all Booking entries related to these tourists
    bookings = Booking.objects.filter(tourist__in=tourists)

    # Pass the data to the template
    return render(request, 'my_booking.html', {
        'bookings': bookings,
        'tourists': tourists,
    })


def admin_homepage(request):
    return render(request, 'admin_homepage.html')


def team(request):
    return render(request, 'team.html')