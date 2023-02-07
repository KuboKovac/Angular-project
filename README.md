
# Angular-project

<p align="center">
  <img src="https://github.com/KuboKovac/Angular-project/blob/main/server/resource/Logo-Github.png">
</p>

# Desc for backend

### Backend Tasks
- [x] Initialization of server
- [x] Memory database
- [x] CRUD operations for users
- [x] CRUD operations for cars
- [ ] Store token into database
- [x] Imporve login
- [ ] Implement swagger
- [x] drink more than 10 coffees☕

**Current progress `75%`**

### How to start a server ?
- 1.First we will need python. **Not older than 3.9 ![Download Here!🐍](https://www.python.org/downloads/release/python-3110/0)**
- 2.Open the folder where the file main.py is located, through the command line
- 3.Type script into console ```Python main.py```

*A Virtual Environment is required for this server*
      <sup>SERVER IS NOT BUILDED YET</sup>

   
### Server Paths:
   ```
   -login and user path
    🟡   [POST]   0.0.0.0:6969/login
    🟢   [GET]    0.0.0.0:6969/user/all
    🟢   [GET]    0.0.0.0:6969/user/<id>
    🟡   [POST]   0.0.0.0:6969/user/new
    🔴   [DEL]    0.0.0.0:6969/user/delete/<id>
    🔵   [PUT]    0.0.0.0:6969/user/update/<id>
    
    -car paths
    🟢   [GET]    0.0.0.0:6969/car/<id>
    🟢   [GET]    0.0.0.0:6969/car/all
    🟡   [POST]   0.0.0.0:6969/car/new
    🔴   [DEL]    0.0.0.0:6969/car/delete/<id>
    🔵   [PUT]    0.0.0.0:6969/car/update/<id>
   ```
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

### Add new car
```
  {
    "id": 1,
    "vehicleModel": "KOLT",
    "vehicleBrand": "MITSUBIŠI",
    "licensePlate": "SOKERES",
    "imageUrl": "www.gugl.com/image.jpg",
    "owner": "Števko"
}
```

### Update car example

```
  {
    "id": 1,
    "vehicleModel": "KOLT",
    "vehicleBrand": "MITSUBIŠI",
    "licensePlate": "SOKERES",
    "imageUrl": "www.gugl.com/image.jpg",
    "owner": "Števko"
}
```
# license
### KASV
