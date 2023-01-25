from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import os
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect #Add this

# Create your views here.
from .models import AirlineSeat
from .models import Passenger

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


def login(request):
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
        return render(request, "registration/login.html")


def logout(request):
    auth.logout(request)
    return redirect('home')


def dashboard_view(request):
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'input_seat.txt')  # full path to text.
    with open(file_path, 'r') as f:
        ls = f.readlines()[1:]
        for l in ls:
            # splitting the seats line by line
            data = l.split()
            for i in data:
                count = int(data[0])
                # print("count", count)
                # print(data)
                # print(i)
                # Create an empty instance of your model
                obj = AirlineSeat()
                # Populate the fields of the model based on the record line
                if (i == 'A' and 0 < count <= 3) or (i == 'F' and 0 < count < 3):
                    seatno = str(count) + i
                    print(seatno)
                    obj.seat_number = seatno
                    obj.seat_class = '1'
                    obj.seat_location = '1'
                    obj.save()
                elif (i == 'B' and 0 < count <= 3) or (i == 'E' and 0 < count < 3):
                    seatno = str(count) + i
                    obj.seat_number = seatno
                    obj.seat_class = '1'
                    obj.seat_location = '2'
                    obj.save()
                elif (i == 'C' and 0 < count <= 3) or (i == 'D' and 0 < count < 3):
                    seatno = str(count) + i
                    obj.seat_number = seatno
                    obj.seat_class = '1'
                    obj.seat_location = '3'
                    obj.save()
                elif (i == 'A' and 3 < count <= 6) or (i == 'F' and 3 <= count < 6):
                    seatno = str(count) + str(i)
                    obj.seat_number = seatno
                    obj.seat_class = '2'
                    obj.seat_location = '1'
                    obj.save()
                elif (i == 'B' and 3 < count <= 6) or (i == 'E' and 3 <= count < 6):
                    seatno = str(count) + str(i)
                    obj.seat_number = seatno
                    obj.seat_class = '2'
                    obj.seat_location = '2'
                    obj.save()
                elif (i == 'C' and 3 < count <= 6) or (i == 'D' and 3 <= count < 6):
                    seatno = str(count) + str(i)
                    obj.seat_number = seatno
                    obj.seat_class = '2'
                    obj.seat_location = '3'
                    obj.save()
                elif (i == 'A' and count > 6) or (i == 'F' and count >= 6):
                    seatno = str(count) + str(i)
                    obj.seat_number = seatno
                    obj.seat_class = '3'
                    obj.seat_location = '1'
                    obj.save()
                elif (i == 'B' and count > 6) or (i == 'E' and count >= 6):
                    seatno = str(count) + str(i)
                    obj.seat_number = seatno
                    obj.seat_class = '3'
                    obj.seat_location = '2'
                    obj.save()
                elif (i == 'C' and count > 6) or (i == 'D' and count >= 6):
                    seatno = str(count) + str(i)
                    obj.seat_number = seatno
                    obj.seat_class = '3'
                    obj.seat_location = '3'
                    obj.save()
    # print("I am here")

    return render(request, 'registration/dashboard.html')


def seat_view(request):
    seat_list = AirlineSeat.objects.all()
    # Sort in ascending order
    newseat_list = list(sorted(seat_list, key=lambda obj: obj.seat_number))

    return render(request, 'registration/seat_view.html', {'seat_list': newseat_list})


def confirmed_view(request):
    # send a seat confirmation email)
    # the variables used come from the registration function
    # have to figure out how to import the variables from registration function

    # https://www.youtube.com/watch?v=xNqnHmXIuzU
    '''send_mail(
        'Account confirmation' + first_name + last_name,  # subject
        'Thank you for signing up to our airline reservation system!',  # message
        [miri.cbe @ gmail.com],  # from email
        email,  # To Email
    ) '''

    return render(request, 'registration/confirmed.html')

def base(request):
    return render(request, 'registration/base.html')

def help(request):
    return render(request,'registration/help.html')

def seat_test(request):
    seat_list = AirlineSeat.objects.all()
    return render(request, 'registration/seat_test.html', {'seat_list': seat_list})

def statistics(request):
    #Counting taken and available Seats

    #available_count = AirlineSeat.seat_flag.all()
    #reserved_count = AirlineSeat.objects.SeatFlags(models.RED).count

    #Percentage of taken and available Seats

    #available_percentage = (available_count / 60) * 100
    #reserved_percentage = (reserved_count / 60) * 100

    #Listing taken and available Seats

    #available_list = AirlineSeat.objects.SeatFlags(models.GREY)
    #reserved_list = AirlineSeat.objects.SeatFlags(models.RED)

    #Counting the Users

    #user_count = Passenger.objects.all().count

    #Listing User and their information

    #user_list = Passenger.objects.all()

    return render(request, 'registration/statistics.html',
    {#'available_count': available_count,
    #'reserved_count': reserved_count,
    #'available_list': available_list,
    #'reserved_list': reserved_list,
    #'user_list': user_list
    })

def seat_simple(request):

    # current issue is saving the altered seat_flag into the database, because every time theres a new input
    # of a seat the flag of the seat inputed before gets resetted to 3(available)

    # still have to figure out how to pass the selected_seat to the html to include in the if


    seat_list = AirlineSeat.objects.all()
    # Sort in ascending order
    newseat_list = list(sorted(seat_list, key=lambda obj: obj.seat_number))
    #print(type(newseat_list[0])) #<class 'register.models.AirlineSeat'>


    if request.method == "GET":
        selected_seat = request.GET.get("selected_seat")
        print("The seat that has been selected is:", selected_seat)
        # print("HELLOOOOOOOO") # Just checking we are entering the if
        for seat in newseat_list:
            print(seat, selected_seat) # To check the entered seat matches the database seat
            if selected_seat == seat.seat_number:
                print("Matched")
                print("The current flag of", seat.seat_number, "is", seat.seat_flag)
                if seat.seat_flag == '3':
                    seat.seat_flag = 1;
                    # obj.save() # something like this to saved the changed flag into the databse!
                    print("The new flag for this seat is: ", seat.seat_flag)
                elif seat.seat_flag == '1':
                    print("This seat is already taken")
                    print("An error should show up in the html!!")
                    messages.info(request, 'This seat has already been reserved. Please choose another seat.')
                    return redirect('registration/seat_simple.html')
                break
            else:
                print("no Match")




    ''' Less optimal alternative to access the inputed seat from the user  
        seat_input = request.GET  # We save what has been inputed in the page into a variable
        reserved_seat = seat_input.get('selected_seat')  # This is how we access the value entered for the key 'your_seat'
        print('Your reserved seat is:', reserved_seat) '''

    return render(request, 'registration/seat_simple.html', {'seat_list': newseat_list})

def seat_iris(request):
    seat_list = AirlineSeat.objects.all()
    # sort in ascending order
    newseat_list = list(sorted(seat_list, key=lambda obj: obj.seat_number))
    return render(request, 'registration/seat_iris.html', {'seat_list': newseat_list})

'''def seat_selection(request):
    seat_list = AirlineSeat.objects.all()
    newseat_list = list(sorted(seat_list, key=lambda obj: obj.seat_number))
    if request.method=='POST':
        seat_selected = request.POST['seat_selected']
        if seat_selected in newseat_list:
            newseat_list'''

def testing(request):
    input = request.GET  # We save what has been inputed in the page into a variable
    person_name = input.get('your_name')  # This is how we access the value entered for the key 'your_seat'
    print('Your name is:', person_name)

    # Since we are working with a QueryDict, this is how we access the keys
    keys = input.keys()
    print("These are the keys stored in the QueryDict: ", keys)

    return render(request, 'registration/testing.html')