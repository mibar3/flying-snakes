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
    path('seat_test', views.seat_test, name='seat_test'),
    path('your_template', views.your_template, name='your_template'),
    path('statistics', views.statistics, name='statistics'),
    path('seat_simple', views.seat_simple, name='seat_simple'),
    path('seat_iris', views.seat_iris, name='seat_iris'),
]
