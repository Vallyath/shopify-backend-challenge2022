Hi! This is my Shopify Backend Coding Challenge 

PRESUMPTIONS: Python and virtualenv are already installed, PostgreSQL also already available to use.

1.  Activate your python virtualenv 
2.  If your terminal is where the requirements.txt exists, 
    input: pip install -r requirements.txt
3.  Using PostgreSQL, create a database called images_api with the following command (only applies to psql shell),
    if using pgAdmin, this would be different): 
    CREATE DATABASE images_api; Afterwards you can use the psql command \c images_api to connect to the database.
    This will allow you to query the table to see if the results have worked or not.
4.  Within backend.py, change app.config['UPLOAD'] path to the upload folder path whatever it may be, 
    for example mine was: '/home/vallyath/shopify-backend-2022/uploads', and then change the path for
    app.config['SQLALCHEMY_DATABASE_URI'], the format is postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]
    for example mine is "postgresql://postgres:putyourdbpasswordhere@localhost:5432/images_api". The default postgres 
    password is "postgres".
5.  Next, you will have to run the following commands in terminal in order:
    1. export FLASK_APP=backend
    2. flask db init
    3. flask db migrate
    4. flask db upgrade
6.  Afterwards, you can finally run the backend python script, I have chosen for it to run on 0.0.0.0 because the default
    web address for flask doesn't work on WSL, then you can use the test.py I have provided to send requests into the server.

Thank you for checking out my code!

