# Back end used:
  - Python
    Framework-Django
Front end:
  - HTML
  - CSS
  - Bootstrap
Database:
  - sqlite3

# A TODO list web application provides a convenient solution for users to organize their tasks.

# Features:

  - **Home page**:
       If the user is authenticated,home page welcome the user with username.If user is not authenticated ,they can only access home page,login page and signup page.Other contents will not be displayed
  - **Create page**:
       In this page the user can Create task with a title and description
  - **List page**:
       In this page the user can view the created tasks with other features:
           -Update : User can update or edit title and description
           -Delete : User can delete each task saperately
  - **Register page**:
        In this page the user can create their accout with a username,email id and password.After sucessfully an account is created,The page will be redirected to Login page
  - **Login page**:
        In this page the user can login to their account with  registered username and password.If they match the page will redirect to Home page
# Admin Dashboard:
    In admin dashboard,the admin can do every action like a normal user

   **Admin Login**
    - Username: admin
    -Password: admin@123


How tho run the app:
   
   Step1: Move to "TODO" Directory
   Step2: env/Scripts/activate   (for activating virtual environment)
   Step3: cd todo_project (project Directory)
   Step4: python manage.py makemigration
   Step5: python manage.py migrate
   Step6: python manage.py runserver
   
  
  
        
       
  