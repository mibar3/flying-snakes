from django.urls import path, include

from . import views

# urls for app

urlpatterns = [
    path('', views.index_view, name='home'),
    path('login/', views.login, name='login'),
    path('form/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('seats', views.seat_view, name='seats'),
    path('confirmed', views.confirmed_view, name='confirmed'),
    path('base', views.base, name='base'),
    path('help', views.help, name='help'),
]
