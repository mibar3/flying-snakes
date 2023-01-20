from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import os
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

# Create your views here.
from .models import AirlineSeat


def index_view(request):
    return render(request, 'registration/index.html')


def register_view(request):
    if request.method == 'POST':  # which get the POST as a request from
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        con_password = request.POST['confirm_password']
        if password == con_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email,
                                                first_name=first_name, last_name=last_name)
                user.set_password(password)  # passing the password to the POST function
                user.save()
                print('success')
                return redirect('')

    else:
        return render(request, 'registration/form.html')


'''def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Invalid Email or Password')
            return redirect('home')
    else:
        return render(request, "registration/login.html")'''


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {user.first_name}.")
                return redirect("seats")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"login_form": form})


def logout(request):
    auth.logout(request)
    return redirect('home')


def dashboard_view(request):
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'input_seat.txt')
    with open(file_path, 'r') as f:
        ls = f.readlines()[1:]
        for l in ls:
            # splitting the seats line by line
            data = l.split()
            #print("data:", data)
            for i in data[1:]:
                count = int(data[0])
                #print('count', count)
                #print('i', i)
                # Create an empty instance of your model
                obj = AirlineSeat()
                if count <= 3:
                    seatno = '0' + str(count) + i
                    if i == 'A' or i == 'F':

                        obj.seat_number = seatno
                        obj.seat_class = '1'
                        obj.seat_location = '1'
                        obj.save()
                    elif i == 'B' or i == 'E':

                        obj.seat_number = seatno
                        obj.seat_class = '1'
                        obj.seat_location = '2'
                        obj.save()
                    else:

                        obj.seat_number = seatno
                        obj.seat_class = '1'
                        obj.seat_location = '3'
                        obj.save()
                if 3 < count <= 6:
                    seatno = '0' + str(count) + i
                    if i == 'A' or i == 'F':
                        obj.seat_number = seatno
                        obj.seat_class = '2'
                        obj.seat_location = '1'
                        obj.save()
                    elif i == 'B' or i == 'E':
                        obj.seat_number = seatno
                        obj.seat_class = '2'
                        obj.seat_location = '2'
                        obj.save()
                    else:
                        obj.seat_number = seatno
                        obj.seat_class = '2'
                        obj.seat_location = '3'
                        obj.save()
                if 6 < count <= 9:
                    seatno = '0' + str(count) + i
                    if i == 'A' or i == 'F':
                        obj.seat_number = seatno
                        obj.seat_class = '3'
                        obj.seat_location = '1'
                        obj.save()
                    elif i == 'B' or i == 'E':
                        obj.seat_number = seatno
                        obj.seat_class = '3'
                        obj.seat_location = '2'
                        obj.save()
                    else:
                        obj.seat_number = seatno
                        obj.seat_class = '3'
                        obj.seat_location = '3'
                        obj.save()
                if count > 9:
                    seatno = str(count) + i
                    if i == 'A' or i == 'F':
                        obj.seat_number = seatno
                        obj.seat_class = '3'
                        obj.seat_location = '1'
                        obj.save()
                    elif i == 'B' or i == 'E':
                        obj.seat_number = seatno
                        obj.seat_class = '3'
                        obj.seat_location = '2'
                        obj.save()
                    else:
                        obj.seat_number = seatno
                        obj.seat_class = '3'
                        obj.seat_location = '3'
                        obj.save()
    # print("I am here")

    return render(request, 'registration/dashboard.html')


def seat_view(request):
    seat_list = AirlineSeat.objects.all()
    # sort in ascending order
    newseat_list = list(sorted(seat_list, key=lambda obj: obj.seat_number))
    return render(request, 'registration/seat_view.html', {'seat_list': newseat_list})


def confirmed_view(request):
    #if confirmed button is clicked, change flag into '1'
    return render(request, 'registration/confirmed.html')
