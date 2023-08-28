from django.urls import path
from . import views

urlpatterns = [
    path('affiliate/', views.affiliate, name='affiliate'),
    path('promo/', views.promo, name='promo'),
    path('new-partner/', views.newPartner, name='new-partner'),
    path('offer-expired/', views.offerExpiry, name='offer-expired')
]
