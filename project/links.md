# Links

https://www.youtube.com/watch?v=4XYsODaQ6Ok (really good overview to refresh django and html :) from 12:37 onwards he shows how to add changes in the website)

## Important!
When running the server, in order to view the seats which are retrieved from a .txt file you must first run the dashboard page. ONLY RUN THE DASHBOARD ONCE, IF YOU RUN IT MORE TIMES THE DATA WILL DUPLICATE EACH TIME. It is only to open the dashboard once, from then on eacht time you run the server the database will have loaded and the seats will show up.

## Database Installation 
https://www.jetbrains.com/help/pycharm/postgresql.html

https://stackoverflow.com/questions/53267642/create-new-local-server-in-pgadmin

Note: Please Use PgAdmin4 for visualization of database

## Django Project setup in Pycharm
https://www.youtube.com/watch?v=krrzQbxgLOE

For me, creating the virtual environment is not working like in this video so here is how I done. Hope this help!
1. Create a project using the new environment setup with the \venv in the end of the virtual environemt project name.
2. Go to File-> New Projects setup-> Preference fro new project-> Python intrepreter-> then choose Python 3.9(venv)
3. After that add packages under that python version. 
4. Packages to add:1. pip 2. django 3. sqlparse
5. Then click apply so that it will be available for that project and in the terminal you will see (venv).

In terminal:
1. pip install django
2. django-admin startproject [project_file_name] (after this command, you will see a file under the project file which include 6/7 python files)
3. cd project_file_name
4. python manage.py runserver

## Postgres steup with Django
https://www.geeksforgeeks.org/how-to-use-postgresql-database-in-django/

Postgresql helps us visualize the data we are creating/working on in SQL language. Here is where we create the table with the airline seats 
https://www.datacamp.com/tutorial/tutorial-postgresql-python

## For starting the simple project
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website

https://www.youtube.com/watch?v=4XYsODaQ6Ok

## Input Data

## Login,Logout

## Display Seats
This shows how to display a sql table from the database (in our case postgresql) onto a website using html
- https://www.youtube.com/watch?v=PhxKV0ax6x8

- https://gist.github.com/aleckyann/98802940060703b9fd99b40e84c2753e (html code for bus seat booking)
- https://sachinkurkute.github.io/movie-seat-layout/src/index.html (interactive! bit javascript)
- https://code-boxx.com/seat-reservation-javascript/
- https://www.youtube.com/watch?v=25AiXy8e09E (to get an idea of how the html code works)
- https://stackoverflow.com/questions/40011399/how-to-layout-something-like-seats-in-cinema-hall (inspo)

## Reserve/Cancel Seats
- https://www.tutorialspoint.com/program-to-implement-seat-reservation-manager-in-python
- https://www.youtube.com/watch?v=ahobllKXEEY (python code)

## Statistics



## Logo Creator
https://www.freelogodesign.org/

## Base.html File for the default setup (navbar,footer, container of the main text)
https://www.youtube.com/watch?v=rjxpL89BEX4

## Fetch Data From a Database And Output To A Webpage (Using pythons classes and atributes)
https://www.youtube.com/watch?v=H3joYTIRqKk

## Creating a branch
https://www.youtube.com/watch?v=QV0kVNvkMxc

## Merging changes in branches and commiting into the main branch
https://www.youtube.com/watch?v=XX-Kct0PfFc
