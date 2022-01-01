# Django InlineAdmin with View Permissions

## Installation

```
python3 -m venv venv
source ./venv/activate
pip install -r requirements.txt
./manage.py migrate
```

## Running the application

```
./manage.py runserver
```

## Notes

The provided database already has a permission group "View Only".
This group contains view only permissions for models defined in
the `home` app.

Following staff users are also present in the database

1. Superuser

   `username`: `admin`

   `password`: `admin`
1. View only user

   `username`: `view-only-user`,

   `password`: `view-only-user`
