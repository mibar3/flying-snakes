from django.urls import path, include

from . import views

# urls for app

urlpatterns = [
    path('', views.index_view, name='home'),
    path('Dashboard/', views.dashboard_view, name='dashboard'),
    path("form/", views.register_view, name='register'),
    # path('login', views.login, name='login'),
    # path('logout', ),
]
