# App Survey Example

## What it is?

- It is just an example of how to use flask as a simple web application.
- It is totally backend, so it ain't matter whatever the client is.
- It is communicate using RESTful, even it doesn't have the full specification of RESTful Web Services.
- It is using json as response, so you can do a lot of things with it.
- It is just for Fun. :D

## What it is again?

- Do you want to learn about Flask?
- Do you want to learn what is BackEnd?
- Do you want to learn what is json?
- Or tell me, what do you want?

## TODO

- Create virtual environment (or not, choose wisely)
- Install all the requirements package/library from requirements.txt `pip install -r requirements.txt`
- Set The Database Uri using shell environment, so if you use (example):
    - Bash/Sh/Zsh: `export DATABASE_URI='postgresql://bugisdev:@localhost/app'`
    - Fish: `set -x DATABASE_URI postgresql://bugisdev:@localhost/app`
- Run the migrate:
    ```python manage.py db upgrade```
- If you changes any models inside models.py, run `python manage.py db migrate` before run the command above.
- And then you ready to rock.
- I'm using PostgreSQL so if you want to use MySQL run `pip install MySQL-Python` and set the Database Uri using MySQL.
- [update] If you want to start the built-in web server, `python manage.py runserver`
- [update] If you want to open the shell, `python manage.py shell`

# Happy Hacking