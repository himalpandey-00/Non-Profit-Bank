from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.LeaderboardListView.as_view(), name='leaderboard-index'),
    #path('<str:pk>/', views.BankDetail.as_view(), name='bank-detail'),
]
