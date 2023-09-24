from django.contrib import admin
from django.urls import path, include
from v1.bank.views import Home
from v1.user.views import UserDetail
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user = True), name = 'login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('v1.user.urls')),
    path('', Home.as_view() , name='index'),
    path('bank/', include('v1.bank.urls')),
    path('donation/', include('v1.donation.urls')),
    path('leaderboard/', include('v1.leaderboard.urls')),
    path('<str:slug>/', UserDetail.as_view(), name='user-profile')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)