# Todo Items API
Todo Items API based on `python3.8` , `Django3.1` , `Django-REST-Framework3.12`

## Features:
1. Register API with first_name,last_name,email,password. API Endpoint-
- (POST) - `https://tododas.herokuapp.com/api/register`
2. User Login API and in response gives JWT Token encoded with first_name,last_name,email,is_active:True/False,Roles:Admin/User. API Endpoint-
- (POST) - `https://tododas.herokuapp.com/api/login` 
3. Todo Items List Operation.Both Admin and User Roles are allowed'. API Endpoint-
- LIST(GET) - `https://tododas.herokuapp.com/api/getall`
4. Todo Items CRUD Operations.Only Admin Roles are allowed. API Endpoints- 
-  CREATE(POST) - `https://tododas.herokuapp.com/api/create`
- RETRIEVE(GET) - `https://tododas.herokuapp.com/api/get/{id}`
- UPDATE(PUT)- `https://tododas.herokuapp.com/api/update/{id}`
- DELETE(DELETE)- `https://tododas.herokuapp.com/api/delete/{id}` 

Note: To run this APIs on Local Server, replace `https://tododas.herokuapp.com` with `http://127.0.0.1:8000`. And {id} is Todo Item ID (primary key) of Todo Item Table.

- Database: PostgresSQL is used

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
To access Django Admin Panel `https://tododas.herokuapp.com/admin` , Use Credentials: 
- Email: admin@admin.in 
- Password: admin

Note:Only Admin can access.

## API Documention:
-Swagger - `https://tododas.herokuapp.com`  
-Docs - `https://tododas.herokuapp.com/redoc` 
