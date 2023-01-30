from django.urls import path, include

from . import views

# urls for app

urlpatterns = [
    path('', views.index_view, name='home'),
    path('login/', views.login_user, name='login'),
    path('form/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout', views.logout_user, name='logout'),
    path('base', views.base, name='base'),
    path('help', views.help, name='help'),
    path('statistics', views.statistics, name='statistics'),
    path('seat_simple', views.seat_simple, name='seat_simple'),
]
