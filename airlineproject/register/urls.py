from django.urls import path, include

from . import views

# urls for app

urlpatterns = [
    path('', views.index_view, name='home'),
    path('login', views.login, name='login'),
    path('form', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout', views.logout_user, name='logout'),
    path('base', views.base, name='base'),
    path('help', views.help, name='help'),
    path('statistics', views.statistics, name='statistics'),
    path('seats', views.seats, name='seats'),
    path('statistics_text', views.statistics_text, name='statistics_text'),
    path('seat_cancellation', views.seat_cancellation, name='seat_cancellation'),
    path('logout_help', views.logout_help, name='logout_help')
]
