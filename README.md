# pdsw22_group_01

### Theint Hay Thi Maung
***
### Miranda Barros
- created the

## Requirements
Pycharm, PgAdmin4, PostgreSQL, Django, html, sql, psycopg2, pip, django-crispy-forms

# How to setup?
Set up in Pycharm
1.Create a project with virtual environemt in Pycharm.
2.Packages need to be installed: Django, html, sql, psycopg2, pip, django-crispy-forms

Create a database to import the data
1. Open up the SQL Shell after having downloaded PostgreSQL. 
2. Use all the default settings (pressing ENTER each time) until you reach the password, for this type in as password "007700". This
is the password that our project uses so that it can sync the data to the database.
3. Name the database, ideally use the name "postgres".

Open up PgAdmin:
1. Enter PgAdmin password 
2. Click on Servers and you will be asked for your PostgreSQL password, use the same password you entered in the SQL Shell: '007700'
3. Click on Databases, so far, an empty database should show up.
4. Now we must run the app, so we can run the dashboard and import the data.
5. Within the repository, type in the terminal:
cd flying-snakes
cd airlineproject
python manage.py runserver

6. Open up the webapp by clicking the localhost direction highlited in blue:http://127.0.0.1:8000/
7.  To run the dashboard, add in the url after the "http://127.0.0.1:8000/dashboard"
8. Then run in the terminal:
 
python manage.py makemigrations register
python manage.py migrate

10.  Now open up PgAdmin and go to Servers > PostgreSQL > postgres > Schemas > public > Tables > register_airlineseat, click on register_airlineseat and then on the "View Data" button next to the Query tool at the top of the page. This should display all the data. 
11.  If this doesnt work and no data shows up, please try migrating first and then running the dashboard.

# Importing seat data and some data from text file

run /dashboard and it will import all the data for seat display from input_seat.txt file and
                   5 user with 1 admin permission from userfile.txt
              
in home, user can register their data. 

In case the dashboard page gets run more than once, the data will double. If this happens, simply go to the register_airlineseat table in PGAdmin, press the Query
tool symbol at the top of the page, and in the box called "Query" type in this command "TRUNCATE TABLE register_airlineseat RESTART IDENTITY;"and then press the play button. This will clean the database and then, if you run the dashboard again, the data should be imported into the database again.


# Code explained

Models: 
1) We use built-in model for handling users data for registration and login,logout part
2) We create a new model AirlineSeat which has seat_number, seat_class, seat_location, seat_price and seat_flag attributes. 
   seat_class has 4 types (First, Business, Economy, Emergency but we don't use Emergency in this project)
   seat_location has 3 types (Window, Middle, Aisle seats)
   seat_price has 3 prices (50 for first class, 25 for middle class, 10 for economy class)
   seat_flag has 3 choices('1' for taken, '2' for selected, '3' for available but '2' is not used in this project)
 
 ### How the sorting of seat works?
All the seats are created as objects. The seats are sorted in ascending order in database but not in admin site page. So how we solve is in the function we add 0 infront of the single digit seat. (Eg: 1A -> 01A) 

 After running the migration, these models will create tables in database. 
 
 # Functions:
 ## 1) dashboard_view function:
 In input_seat.txt file, there are 10 rows and 6 columns which is like (A B C D E F)
 It reads the text file and put the data into the register_airlineseat table. The data/seat are objects of AirlineSeat model.
 
 In userfile.txt file, there are 5 rows and 6 columns. Columns are first_name, last_name, email, username, password, is_superuser(0 means yes, 1 means no)
 This function read text file and put all these 5 users into the already existing table from django which is auth_user.
 
 Error handling for dashboard function is if the text file is not in the same format as the example, it will throw the exception.
 
 ## 2) register_view function:
 This function is simply asked the inputs from user as a form. If the username is existed in the database it will redirect to the same page and asked the data from user again. If no, then this user will create in database and redirect the user to home page. 
 
 ***
 
 
