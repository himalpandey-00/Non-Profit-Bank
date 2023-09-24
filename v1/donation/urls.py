from django.urls import path, include
from .views import CreateDonation, ListDonation

urlpatterns = [
    path('', ListDonation.as_view(), name='list-donation'),
    path('<str:pk>/add/', CreateDonation.as_view(), name='add-donation'),
]