from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('enquiry/', views.contact_enquiry, name='enquiry'),
]
