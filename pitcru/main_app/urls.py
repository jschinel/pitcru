from django.urls import path
from . import views

urlpatterns = [
    path('cars/<int:car_id>/', views.cars_detail, name='details'),
    path('cars/', views.cars, name='cars'),
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
    path('accounts/logout/', views.logout_view, name = 'logout'),
    path('accounts/signup/', views.signup, name='signup')
]
