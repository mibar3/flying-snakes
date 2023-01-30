from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import os
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
            return redirect('seat_simple')
        else:
            messages.info(request, 'Upsi: Your username or password is wrong.')
            return redirect('login')
    else:
        return render(request, "registration/login_test.html")


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out!')
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
    # Sort in ascending order
    newseat_list = list(sorted(seat_list, key=lambda obj: obj.seat_number))
    # print(type(newseat_list[0])) #<class 'register.models.AirlineSeat'>

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


def seat_simple(request):

    # still have to figure out how to pass the selected_seat to the html to include in the if
    seat_list = AirlineSeat.objects.all()
    # Sort in ascending order
    newseat_list = list(sorted(seat_list, key=lambda obj: obj.seat_number))
    # print(type(newseat_list[0])) #<class 'register.models.AirlineSeat'>



    if request.method == "GET":
        count = 0
        selected_seat = request.GET.get("selected_seat")

        for seat in newseat_list:
            count+=1
            if selected_seat == seat.seat_number:
                print("The seat that has been selected is:", selected_seat)
                print(seat, selected_seat)  # To check the entered seat matches the database seat
                print("It's a match!")
                print("The current flag of", seat.seat_number, "is", seat.seat_flag)

                if seat.seat_flag == '3':
                    seat.seat_flag = '1';
                    seat.save() # this saves the change in the database but when i input
                    # the seat again after changing its flag the website crashes
                    print("The new flag for this seat is: ", seat.seat_flag)

                elif seat.seat_flag == '1':
                    ''' seat.seat_flag = '3'; # to reset any seat that has been reserved after testing
                    seat.save() '''
                    print("This seat is already taken")
                    messages.info(request, 'This seat has already been reserved. Please choose another seat.')
                    return redirect('/seat_simple')
                break

            else:
                print(seat, selected_seat)
                print("no match")

    print(count)
    ''' No funciona manda miles de requests ! 
    if count  == 60:
        messages.info(request, 'Please enter a valid seat number.')
        return redirect('/seat_simple') '''




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