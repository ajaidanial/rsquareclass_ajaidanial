# Task 1 | Rsquare

## Prerequisites

1. python3
2. pip3
3. virtualenv

### Linux
`sudo apt install python3 python3-pip virtualenv libpq-dev python3-dev build-essential postgresql-server-dev-all`

### Mac
`brew install python3`
`pip3 install virtualenv`

## Running Locally

Use the command `./start`

If the above command fails follow the steps:
1. `virtualenv -p python3 venv`
2. `. venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python manage.py makemigrations`
5. `python manage.py migrate`
6. `python manage.py collectstatic`
7. Set the proper environmental variables in `.env` file
8. `python manage.py runserver`
