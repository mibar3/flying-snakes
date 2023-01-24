from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import os
from django.core.mail import send_mail

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

    if request.method == "POST":
        display_type = request.POST.get("display_type", None)
        if display_type in ["selected_seat"]:
            print('The name that was typed in is:')
            print(request.POST)
            # Handle whichever was selected here

    return render(request, 'registration/seat_view.html', {'seat_list': seat_list})


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


''' This is the code is used from https://www.geeksforgeeks.org/render-html-forms-get-post-in-django/ 
    to test the get post in html'''
def your_template(request):
    # logic of view will be implemented here
    print('The name that was typed in is:')
    print(request.POST)
    return render(request, 'registration/your_template.html')


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
    seat_list = AirlineSeat.objects.all()
    # Sort in ascending order
    newseat_list = list(sorted(seat_list, key=lambda obj: obj.seat_number))
    #print(type(newseat_list[0])) #<class 'register.models.AirlineSeat'>
    print(newseat_list)


    ''' IGNORE THIS COMMENTED STUFF
    
    # CLEANING UP THE LIST, MANY VALUES WHERE REPEATED MULTIPLE TIMES
    first_half, second_half = newseat_list[:71], newseat_list[72:]
    del second_half[::2] # deletes every second item because each seat number is repeated one until 9F
    # i had to separate the newseat_list because the values were doubled, first 01A, 02B, etc, until 10F
    # then the values started again at 1A, 2B but ended in 9F
    # print(f'{first_half=}')
    # print("THIS IS WHERE THE FIRST HALF ENDS")
    # print(f'{second_half=}')

    row_10_first_half = first_half[54:]
    del row_10_first_half[::3] # first delete every third value, because from 10A onwards every seat is repeated thrice
    del row_10_first_half[::2] # once every row from 10A onwards only repeated twice, delete every second item
    #print(f'{row_10_first_half=}')
    # here i took the row 10 from the first half and added it to the list with 1A, 2A, etc.
    second_half.extend(row_10_first_half)
    # print(second_half)

    # END OF CLEANING THE LIST

    selected_seat = request.POST # We save what has been inputed in the page into a variable
    selected_seat = selected_seat.get('your_seat') # This is how we access the value entered for the key 'your_seat'
    print('The seat to be reserved is:', selected_seat)
    print(type(second_half)) '''




    # Since we are working with a QueryDict, this is how we access the keys
    #keys = selected_seat.keys()
    #print("These are the keys stored in the QueryDict: ", keys)


    if "AirlineSeat: 9C" in second_half:
        print("Object exists in the dictionary")
    else:
        print("Object does not exist in the dictionary")

    '''if selected_seat in newseat_list:
        print("this seat should become unavailable!")
        # change the flag of the seat, i am unsure of how to access the seat number of an object
    '''
    # if selected seat != ... for the case that an invalid value is typed in
        # print()



    if request.method == "POST":
        selected_seat = request.POST.get("selected_seat", None)
        if selected_seat in newseat_list:
            print('The seat that has been selected is:')
            print(request.POST)
            # Change flag of whichever was selected here

    return render(request, 'registration/seat_simple.html', {'seat_list': newseat_list})