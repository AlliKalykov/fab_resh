# Quiz

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/AlliKalykov/fab_resh.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv venv
$ source env/bin/activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ python manage.py migrate
(venv)$ python manage.py createsuperuser
(venv)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

Navigate to `http://127.0.0.1:8000/swagger/` for watch API's.