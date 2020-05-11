### Environment Setup

#### Create postgres container

This will get the postgres container running with a default database called 'basic_ecomm'. Make sure you have docker and docker-compose installed in your system.

```
$ cd development
$ sudo docker-compose up
```

#### Development setup

- Install python3 and python3-venv

```
$ sudo apt install python3 python3-venv
```

- Create virtual env, activate and install requirements

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

- In project root, copy .env.template as .env and configure all environment variables

- Run first migrations

```
$ python manage.py migrate
```

- Create superuser

```
$ python manage.py createsuperuser
```

- And finally, run the server with:

```
$ python manage.py runserver
```
