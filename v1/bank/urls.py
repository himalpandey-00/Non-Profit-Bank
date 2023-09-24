from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BankList.as_view(), name='bank-index'),
    path('<str:pk>/', views.BankDetail.as_view(), name='bank-detail'),
]
