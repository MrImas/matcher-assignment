## Ofir Imas

# Gloat Backend Home Assignment - Basic Matcher

## Overview:

# Implement a basic web server with MySQL called “matcher”.

# You should create a MySQL connection on port 3307 (or any other port you want just change the setting.py file under /gloatassingment folder)

# create database with the name 'matcher' (again, can change to whatever name you'd like, just change the settings as well)

# create user 'test_matcher' with password 'test123'

# grant all priviliges to the user

# run in the cmd python manage.py makemigrations

# run in the cmd python manage.py migrate

## Run the server with the following command:

### $ python manage.py runserver

### url - '/jobs/' -> will display all jobs available

### url - '/jobs/<int:job_id>' -> will display all matching candidate for the job with <job_id>

### You can add the query parameter 'top' for choosing the number of top matching candidates

### for example: url - '/jobs/1?top=50 -> will find top 50 candidates for the job with id 1

## Thanks in advance for the opportunity!
