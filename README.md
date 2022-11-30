# Angular-project

# Desc for backend

### urls:
    [POST]0.0.0.0:6969/login
    [GET]0.0.0.0:6969/user/all
    [GET]0.0.0.0:6969/user/<id>
    [POST]0.0.0.0:6969/user/new
    [DEL]0.0.0.0:6969/user/delete/<id>
    [PUT]0.0.0.0:6969/user/update/<id>

### Login body example
   ```
   {"username":"Imhotep","password":"Husak"}
   ```
   admin credentials: 
   admin username: **Imhotep**
   admin password: **Husak**

### Create new user
    {"username":"pišta","password":"123"}
    


### Update body example
   
    {"id": 2, "username": "Kamil", "password": "Husak", "role": "Guest"}
