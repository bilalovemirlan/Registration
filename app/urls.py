from django.urls import path
from .views import *
from django.views.generic import RedirectView



urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('favicon\.ico',RedirectView.as_view(url='/static/images/favicon.ico')),
]