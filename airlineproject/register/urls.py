from django.urls import path, include

from . import views

# urls for app

urlpatterns = [
    path('', views.index_view, name='home'),
    path('login/', views.login_user, name='login'),
    path('form/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout', views.logout_user, name='logout'),
    path('seats', views.seat_view, name='seats'),
    path('confirmed', views.confirmed_view, name='confirmed'),
    path('base', views.base, name='base'),
    path('help', views.help, name='help'),
    path('seat_test', views.seat_test, name='seat_test'),
    path('statistics', views.statistics, name='statistics'),
    path('seat_simple', views.seat_simple, name='seat_simple'),
    path('seat_iris', views.seat_iris, name='seat_iris'),
    path('testing', views.testing, name='testing'),
]
