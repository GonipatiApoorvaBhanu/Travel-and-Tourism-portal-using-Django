"""Tourism URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Travel import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),   # Login page
    path('logout/', views.login_view, name='logout'),
    path('available-buses/', views.available_buses, name='available_buses'),
    path('book-bus/<int:bus_id>/', views.book_bus, name='book_bus'),
    path('about/', views.about_view, name='about'),
    path('tours/', views.tour_list, name='tour_list'),
    path('tour/<int:tour_id>/', views.tour_details, name='tour_details'),
    path('payment-form/', views.payment_form, name='payment_form'),
    path('payment-success/<int:bus_id>/', views.payment_success, name='payment_success'),
    path('buses/', views.home_view, name='buses'), 
    path('buses/<int:tour_id>/', views.buses, name='buses'),
     path('booking-success/<int:bus_id>/', views.booking_success, name='booking_success'),
     path('buses/<int:bus_id>/payment/', views.payment_form, name='payment_form'),

     
]
