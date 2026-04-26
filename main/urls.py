from django.urls import path
from . import views


urlpatterns = [
    path('',  views.home, name='home_main'),
    path('about/', views.about, name='about_main'),
    path('contact/', views.ContactView.as_view(), name='contact_main'),
    path('service/', views.ServiceView.as_view(), name='service_main'),
]
