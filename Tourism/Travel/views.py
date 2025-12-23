from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login,logout
from .models import Bus, Tour
from . import views
from .models import Tour
from django.contrib.auth.decorators import login_required
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')

        else:
            error = 'Invalid username or password'

    return render(request, 'login.html', {'error': error})

@login_required(login_url='login')
def home_view(request):
    destinations = Tour.objects.values_list('location', flat=True).distinct()
    return render(request, 'home.html', {
        'destinations': destinations,
        'show_footer': True,
    })

def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('login')
def about_view(request):
    return render(request, 'about.html')

def tour_list(request):
    tours = Tour.objects.all()
    return render(request, 'tour_list.html', {'tours': tours})

def tour_details(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    return render(request, 'tour_details.html', {'tour': tour})

def available_buses(request):
    destination = request.GET.get('destination', '')
    guests = request.GET.get('guests', '')

    buses = Bus.objects.filter(destination__icontains=destination)

    return render(request, 'available_buses.html', {
        'buses': buses,
        'destination': destination,
        'guests': guests,
    })



def tour_list(request):
    destination = request.GET.get('destination', '')

    if destination:
        tours = Tour.objects.filter(location__icontains=destination)
    else:
        tours = Tour.objects.all()

    return render(request, 'tour_list.html', {
        'tours': tours,
        'destination': destination,
    })



def buses(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    buses = Bus.objects.filter(tour=tour)
    return render(request, 'buses.html', {'tour': tour, 'buses': buses})  
      
from django.shortcuts import get_object_or_404, redirect
from Travel.models import Bus


from .models import Bus

def book_bus(request, bus_id):
    bus = get_object_or_404(Bus, id=bus_id)
    
    # Example logic: decrease seats (optional)
    if bus.seats > 0:
        bus.seats -= 1
        bus.save()
    
    # Redirect with the correct argument
    return redirect('booking_success', bus_id=bus.id)        
def booking_success(request, bus_id):
    bus = get_object_or_404(Bus, id=bus_id)
    return render(request, 'booking_success.html', {'bus': bus})

def payment_form(request, bus_id):
    bus = get_object_or_404(Bus, id=bus_id)
    error = ''

    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvv = request.POST.get('cvv')

        if card_number and expiry_date and cvv:
            # Proceed to payment success page
            return redirect('payment_success', bus_id=bus.id)
        else:
            error = 'All fields are required!'

    return render(request, 'payment_form.html', {'bus': bus, 'error': error})            
    
    return render(request, 'payment_form.html', {'bus': bus, 'error': error})    
def payment_success(request, bus_id):
    return render(request, 'payment_success.html', {'bus_id': bus_id})

