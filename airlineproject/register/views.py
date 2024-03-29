import time

from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import os
from django.contrib.auth.decorators import permission_required, login_required
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect #Add this


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
                return redirect('home')

    else:
        return render(request, 'registration/form.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('seats')
        else:
            messages.info(request, 'Upsi: Your username or password is wrong.')
            return redirect('login')
    else:
        return render(request, "registration/login.html")


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out!')
    return redirect('home')


def logout_help(request):
    return render(request, "registration/logout_help.html")

def dashboard_view(request):
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'input_seat.txt')
    try:
        with open(file_path, 'r') as f:
            ls = f.readlines()[1:]
            for l in ls:
                # splitting the seats line by line
                data = l.split()
                # print("data:", data)
                for i in data[1:]:
                    count = int(data[0])
                    # print('count', count)
                    # print('i', i)
                    # Create an empty instance of your model
                    obj = AirlineSeat()
                    if count <= 3:
                        seatno = '0' + str(count) + i
                        if i == 'A' or i == 'F':
                            obj.seat_number = seatno
                            obj.seat_class = '1'
                            obj.seat_location = '1'
                            obj.seat_price = '1'
                            obj.save()
                        elif i == 'B' or i == 'E':
                            obj.seat_number = seatno
                            obj.seat_class = '1'
                            obj.seat_location = '2'
                            obj.seat_price = '1'
                            obj.save()
                        else:
                            obj.seat_number = seatno
                            obj.seat_class = '1'
                            obj.seat_location = '3'
                            obj.seat_price = '1'
                            obj.save()
                    if 3 < count <= 6:
                        seatno = '0' + str(count) + i
                        if i == 'A' or i == 'F':
                            obj.seat_number = seatno
                            obj.seat_class = '2'
                            obj.seat_location = '1'
                            obj.seat_price = '2'
                            obj.save()
                        elif i == 'B' or i == 'E':
                            obj.seat_number = seatno
                            obj.seat_class = '2'
                            obj.seat_location = '2'
                            obj.seat_price = '2'
                            obj.save()
                        else:
                            obj.seat_number = seatno
                            obj.seat_class = '2'
                            obj.seat_location = '3'
                            obj.seat_price = '2'
                            obj.save()
                    if 6 < count <= 9:
                        seatno = '0' + str(count) + i
                        if i == 'A' or i == 'F':
                            obj.seat_number = seatno
                            obj.seat_class = '3'
                            obj.seat_location = '1'
                            obj.seat_price = '3'
                            obj.save()
                        elif i == 'B' or i == 'E':
                            obj.seat_number = seatno
                            obj.seat_class = '3'
                            obj.seat_location = '2'
                            obj.seat_price = '3'
                            obj.save()
                        else:
                            obj.seat_number = seatno
                            obj.seat_class = '3'
                            obj.seat_location = '3'
                            obj.seat_price = '3'
                            obj.save()
                    if count > 9:
                        seatno = str(count) + i
                        if i == 'A' or i == 'F':
                            obj.seat_number = seatno
                            obj.seat_class = '3'
                            obj.seat_location = '1'
                            obj.seat_price = '3'
                            obj.save()
                        elif i == 'B' or i == 'E':
                            obj.seat_number = seatno
                            obj.seat_class = '3'
                            obj.seat_location = '2'
                            # obj.seat_price = '3'
                            obj.save()
                        else:
                            obj.seat_number = seatno
                            obj.seat_class = '3'
                            obj.seat_location = '3'
                            obj.seat_price = '3'
                            obj.save()
    except:
        print("Something wrong with the format in seat text file")

    # print("I am here")
    user_file_path = os.path.join(module_dir, 'userfile.txt')
    try:
        with open(user_file_path, 'r') as f:
            ls = f.readlines()
            for l in ls:
                # splitting the seats line by line
                data = l.split()
                # print(data)
                # print("data:", data)
                if data[5] == '0':
                    user = User.objects.create_user(username=data[3], password=data[4], email=data[2],
                                                    first_name=data[0], last_name=data[1], is_superuser=True)
                    user.set_password(data[4])  # passing the password to the POST function
                    user.save()
                    print('success')
                else:
                    user = User.objects.create_user(username=data[3], password=data[4], email=data[2],
                                                    first_name=data[0], last_name=data[1])
                    user.set_password(data[4])  # passing the password to the POST function
                    user.save()
                    print('success')
    except:
        print("Something wrong with the format in userdata file")

    return render(request, 'registration/dashboard.html')

def base(request):
    return render(request, 'registration/base.html')

def help(request):
    return render(request,'registration/help.html')

@permission_required('is.superuser')
def statistics(request):
    #Counting taken and available Seats
    seat_count = AirlineSeat.objects.all().count()

    available_count = AirlineSeat.objects.filter(seat_flag=3).count()
    reserved_count = AirlineSeat.objects.filter(seat_flag=1).count()

    #Percentage of taken and available Seats

    available_percentage = round((available_count/seat_count) * 100)
    reserved_percentage = round((reserved_count/seat_count) * 100)

    #Listing taken and available Seats

    available_list = AirlineSeat.objects.filter(seat_flag=3)
    reserved_list = AirlineSeat.objects.filter(seat_flag=1)

    #Counting the Users

    #user_count = Users.objects.all().count

    count_users = User.objects.values().count

    #Listing User and their information

    all_users = User.objects.values()

    return render(request, 'registration/statistics.html',
    {'seat_count': seat_count,
    'available_count': available_count,
    'reserved_count': reserved_count,
    'available_percentage':available_percentage,
    'reserved_percentage':reserved_percentage,
    'available_list': available_list,
    'reserved_list': reserved_list,
    'count_users': count_users,
    'all_users': all_users,
    })

@permission_required('is.superuser')
def statistics_text(request):
    response = HttpResponse(content_type='text/plaibn')
    response['Content-Disposition'] = 'attachment; filename=statistics.txt'

    seat_count = AirlineSeat.objects.all().count()

    available_count = AirlineSeat.objects.filter(seat_flag=3).count()
    reserved_count = AirlineSeat.objects.filter(seat_flag=1).count()

    available_percentage = round((available_count / seat_count) * 100)
    reserved_percentage = round((reserved_count / seat_count) * 100)

    available_list = AirlineSeat.objects.filter(seat_flag=3)
    reserved_list = AirlineSeat.objects.filter(seat_flag=1)

    count_users = User.objects.values().count()
    all_users = User.objects.values()

    available_seat_list_text=[]
    taken_seat_list_text=[]
    user_info_text=[]

    lines = ['Number of Seats:\n'
             'available Seats:', available_count,'(',available_percentage,'%)\n',
             'taken Seats:', reserved_count,'(', reserved_percentage,'%)\n',
             'List of Seats:\n'
             'available Seats:', available_seat_list_text, '\n'
             'taken Seats:', taken_seat_list_text, '\n'                                            
             'User Information:\n',
             'Number of Users:', count_users, '\n',
             'User:', user_info_text, '\n',
             ]

    for seat in available_list:
        available_seat_list_text.append({seat.seat_number})
    for seat in reserved_list:
        taken_seat_list_text.append({seat.seat_number})
    for user in all_users:
        user_info_text += (user['username'],user['first_name'],user['last_name'],user['email'])


    response.writelines(lines)
    return response


@login_required()
def seats(request):
    seat_list = AirlineSeat.objects.all()
    # Sort in ascending order
    newseat_list = list(sorted(seat_list, key=lambda obj: obj.seat_number))
    # print(type(newseat_list[0])) #<class 'register.models.AirlineSeat'>

    if request.method == "GET":
        selected_seat = request.GET.get("selected_seat") # The users input gets saved into a string
        selected_seat_with_zero_in_front = "0"+str(selected_seat) # Add a zero before the input to match the database
        count = 0

        for seat in newseat_list:
            if selected_seat_with_zero_in_front == "0None":
                break

            if len(selected_seat_with_zero_in_front) > 4:
                messages.info(request, 'Please enter a valid seat.')
                return redirect('/seats')

            if selected_seat_with_zero_in_front.isdigit():
                messages.info(request, 'Please enter a valid seat.')
                return redirect('/seats')

            elif selected_seat_with_zero_in_front == seat.seat_number:
                print("The seat that has been selected is:", selected_seat_with_zero_in_front)
                print(seat, selected_seat_with_zero_in_front)  # To check the entered seat matches the database seat
                print("It's a match!")
                print("The current flag of", seat.seat_number, "is", seat.seat_flag)

                if seat.seat_flag == '3':
                    seat.seat_flag = '1';
                    seat.save() # This saves the change in the database but when i input
                    # The seat again after changing its flag the website crashes
                    print("The new flag for this seat is: ", seat.seat_flag)
                    messages.info(request, 'Thank you! The seat you have selected has been successfully reserved.')
                    return redirect('/seats')

                elif seat.seat_flag == '1':
                    ''' seat.seat_flag = '3'; # to reset any seat that has been reserved after testing
                    seat.save() '''
                    print("This seat is already taken")
                    messages.info(request, 'This seat has already been reserved. Please choose another seat.')
                    return redirect('/seats')

            else:
                print(seat, selected_seat_with_zero_in_front)
                print("no match")
                count+=1

    return render(request, 'registration/seats.html', {'seat_list': newseat_list})

@permission_required('is.superuser')
def seat_cancellation(request):
    # still have to figure out how to pass the selected_seat to the html to include in the if
    seat_list = AirlineSeat.objects.all()
    # Sort in ascending order
    newseat_list = list(sorted(seat_list, key=lambda obj: obj.seat_number))
    # print(type(newseat_list[0])) #<class 'register.models.AirlineSeat'>

    if request.method == "GET":
        selected_seat = request.GET.get("selected_seat")
        selected_seat_with_zero_in_front = "0"+str(selected_seat) # Add a zero before the input to match the database

        for seat in newseat_list:
            if selected_seat_with_zero_in_front == seat.seat_number:

                if seat.seat_flag == '1':
                    seat.seat_flag = '3';
                    seat.save()  # this saves the change in the database but when i input
                    # the seat again after changing its flag the website crashes
                    print("The seat is available again:", seat.seat_flag)
                    messages.info(request, 'This seat has become available again.')
                    return redirect('/seat_cancellation')
                elif seat.seat_flag == '3':
                    print("The seat is already available: ", seat.seat_flag)
                    messages.info(request, 'This seat is already available.')
                    return redirect('/seat_cancellation')

            else:
                print(seat, selected_seat_with_zero_in_front)
                print("no match")

    return render(request, 'registration/seat_cancellation.html', {'seat_list': newseat_list})



