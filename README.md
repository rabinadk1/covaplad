# covaplad

This repo contains the source code for the **COVID Volunteer and Plasma Donor** system. This was an academic project assigned by the [**Department of Electronics and Computer Engineering, Pulchowk Campus** ](http://doece.pcampus.edu.np/) under the subject _Database Management System_.

## Technologies Used

1. [Django](https://www.djangoproject.com/) for the backend system
2. [MariaDB](https://mariadb.org/) for the database server
3. HTML, CSS, and little bit of vanilla ES5 Javascript for making AJAX requests

## Usage

### Install necessary requirements

You need to have [_python_](https://www.python.org/) as well as _pip_ installed in your system to run this project. [_MariaDB_](https://mariadb.org/) also need to be explicitly installed and configured as per your convinience. You can also install [XAMPP](https://www.apachefriends.org/index.html), which comes with [MariaDB](https://mariadb.org/) and [PHPMyAdmin](https://www.phpmyadmin.net/), if you do not like to tinker much with your system.

To install python dependencies, follow the following steps. _Note: The following instructions assumed you have **Python 3** for the `python` command._

**Create a virtual environment**

`python -m venv .venv`

**Activate the environment**

Assuming you are using _bash_ or _zsh_

`source .venv/bin/activate`

**Install python dependencies**

`pip install -r requirements.txt`

### Create a Database

First create a database in MariadDB and keep a file with name `database.conf` in the root of the project with the contents similar to below.

```
[client]
database = covaplad
user = covaplad
password = <secret_key>
default-character-set = utf8
```

The database field above is the name of the database you just created, and user and password field is the username and the password of the user with all the previledges to the database just created.

### Make changes to the database

To migrate the necessary changes to the newly created database run the following command.

`./manage.py migrate`

NOTE: This only propagates the changes to the database schema to your newly created database. It doesn't add any data entries to the database. For a sample of data entries please contact the team.

### First Time setup
During the first time setup, the **admin user** should be created from the python shell. So in order to create an admin user, run the following command from the project root directory.

`./manage.py shell`

This opens an interactive python shell. In the python shell, enter the following line by line.

```python
from address.models import *
from user.models import User
from datetime import date

c = Country(name="Nepal")
c.save()
p = Province(name="Bagmati Pradesh", country=c)
p.save()
d = District(name="Kathmandu", province=p)
d.save()
m = Municipality(name="Nagarjun", district=d)
m.save()
w = Ward(number=1, municipality=m)
w.save()


user = User(username="admin",first_name="Ram", middle_name="Bahadur", last_name="Thami", email="admin@covaplad.com", phone_number=9860807667,gender="M", temporary_address=w, permanent_address=w)
user.set_password("admin")
user.dob = date(1999,1,1)
user.is_superuser=True
user.is_staff=True
user.save()
```

Now an admin user with username `admin` and password `admin` is created. You can visit the admin site by going to `/admin` in the website if you are logged in as the admin

### Run Backend Server

Now the schema of various tables are setup in your newly created database. You can now run the database server using the following command.

`./manage.py runserver`

This will run a development server in localhost on port 8000. The development server will not be accessible on the LAN just now.
