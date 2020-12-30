# covaplad

This repo contains the source code for the **COVID Volunteer and Plasma Donor** system. This was an academic project assigned by the **Department of Electronics and Computer Engineering, Pulchowk Campus** under the subject _Database Management System_.

## Technologies Used

1. [Django](https://www.djangoproject.com/) for the backend system
2. [MariaDB](https://mariadb.org/) for the database server
3. HTML, CSS, and little bit of vanilla ES5 Javascript for making AJAX requests

## Usage

### Install necessary requirements

You need to have _python_ as well as _pip_ installed in your system to run this project. _MariaDB_ also need to be explicitly installed and configured as per your convinience.

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

### Run Backend Server

Now the schema of various tables are setup in your newly created database. You can now run the database server using the following command.

`./manage.py runserver` or `./run.sh`

This will run a development server in localhost on port 8000. The development server will not be accessible on the LAN just now.

