from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.UserFormView.as_view(), name='user-register'),
    path('<int:pk>/settings/', views.UserUpdateView.as_view(), name='user-edit')
    #path('profile/', views.UserProfileUpdate.as_view(), name = 'user-edit'),
    #path('register/email/<str:partial_token>', views.acquire_email , name = 'acquire_email'),
]
