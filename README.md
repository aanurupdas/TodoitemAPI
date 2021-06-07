# Todo Items API
Todo Items API based on `python3.8` , `Django3.1` , `Django-REST-Framework3.12`

## Features:
1. Register API with first_name,last_name,email,password. API Endpoint-
- (POST) - `https://dastodo.herokuapp.com/api/register`
2. User Login API and in response gives JWT Token encoded with first_name,last_name,email,is_active:True/False,Roles:Admin/User. API Endpoint-
- (POST) - `https://dastodo.herokuapp.com/api/login` 
3. Todo Items List Operation.Both Admin and User Roles are allowed'. API Endpoint-
- LIST(GET) - `https://dastodo.herokuapp.com/api/getall`
4. Todo Items CRUD Operations.Only Admin Roles are allowed. API Endpoints- 
-  CREATE(POST) - `https://dastodo.herokuapp.com/api/create`
- RETRIEVE(GET) - `https://dastodo.herokuapp.com/api/get/{id}`
- UPDATE(PUT)- `https://dastodo.herokuapp.com/api/update/{id}`
- DELETE(DELETE)- `https://dastodo.herokuapp.com/api/delete/{id}` 

Note: To run this APIs on Local Server, replace `https://dastodo.herokuapp.com` with `http://127.0.0.1:8000`. And {id} is Todo Item ID (primary key) of Todo Item Table.

## Installation:
On Local Server, Install via pip: 
```bash
pip install -r requirements.txt
```

## Create Table:
On Local Server, Run command in terminal:
```bash
python manage.py migrate
```

## Create SuperUser/Admin Role:
On Local Server, Run command in terminal:
```bash
python manage.py createsuperuser
```

## Start Server
On Local Server,Run command in terminal:
```bash
python manage.py runserver
```
Open Local Server `http://127.0.0.1:8000` in your browser.

## Access Django Admin Panel:
To access Django Admin Panel `https://dastodo.herokuapp.com/admin` , Use Credentials: 
- Email: admin@admin.in 
- Password: admin

Note:Only Admin can access.

## API Documention:
-Swagger - `https://dastodo.herokuapp.com`  
-Docs - `https://dastodo.herokuapp.com/redoc` 
