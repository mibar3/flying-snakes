# pdsw22_group_01

Theint Hay Thi Maung

# Requirement
Pycharm, PgAdmin4

# How to setup?
Set up in Pycharm
1.Create a project with virtual environemt in Pycahrm.
2.Packages need to be installed: Django, html, sql, psycopg2, pip, django-crispy-forms

Set up in PgAdmin4
1. Create database under the main server
2. Change the database name and password in setting.py file 'DATABASES'

# How to run?

In terminal,

cd project_file
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

# Importing seat data and some data from text file

run /dashboard and it will import all the data for seat display from input_seat.txt file and
                   5 user with 1 admin permission from userfile.txt
              
in home, user can register their data. 

# Code explained

Models: 
1) We use built-in model for handling users data for registration and login,logout part
2) We create a new model AirlineSeat which has seat_number, seat_class, seat_location, seat_price and seat_flag attributes. 
   seat_class has 4 types (First, Business, Economy, Emergency but we don't use Emergency in this project)
   seat_location has 3 types (Window, Middle, Aisle seats)
   seat_price has 3 prices (50 for first class, 25 for middle class, 10 for economy class)
   seat_flag has 3 choices('1' for taken, '2' for selected, '3' for available but '2' is not used in this project)
 
 After running the migration, these models will create tables in database. 
 
 # Functions:
 # 1) dashboard_view function:
 In input_seat.txt file, there are 10 rows and 6 columns which is like (A B C D E F)
 It reads the text file and put the data into the register_airlineseat table. 
 
 In userfile.txt file, there are 5 rows and 6 columns. Columns are first_name, last_name, email, username, password, is_superuser(0 means yes, 1 means no)
 This function read text file and put all these 5 users into the already existing table from django which is auth_user.
 
 Error handling for dashboard function is if the text file is not in the same format as the example, it will throw the exception.
 
 # 2) register_view function:
 This function is simply asked the inputs from user as a form. If the username is existed in the database it will redirect to the same page and asked the data from user again. If no, then this user will create in database and redirect the user to home page. 
 
 
 
