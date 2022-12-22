from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index_view(request):
    return render(request, 'registration/index.html')


def dashboard_view(request):
    return render(request, 'registration/dashboard.html')


def register_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        con_password = request.POST['confirm_password']
    else:
        return render(request, 'registration/form.html')
