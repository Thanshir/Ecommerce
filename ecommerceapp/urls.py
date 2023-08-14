from django.contrib import admin
from django.urls import path
from . import views
from akhiauthentic import views as v1

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('profile', views.profile, name="profile"),
    path('contact', views.contact, name="contact"),
    path('checkout', views.checkout, name='checkout'),
    path('handlerequest/', views.handlerequest, name='handlerequest'),
    path('activate/<str:uidb64>/<str:token>/', v1.activate_account, name='activate_account'),
]


