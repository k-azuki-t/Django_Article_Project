from django.urls import path, include
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile_change/', CustomUserUpdateView.as_view(), name='profile_change'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('signup/', RegistrationView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogutView.as_view(), name='logout'),
    path('withdraw/', CustomDeleteView.as_view(), name='withdraw'),
]