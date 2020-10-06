# ghost-todo
Ghost ToDo


## Installation

To install projects you need to follow next steps:

1. clone this repo
1. install virtualenv
1. create virtualenv in the repo
1. install dependecies via pip
1. run

Example script:

```shell
git clone git@github.com:GeorgeZhukov/ghost-todo.git

pip install virtualenv

cd ghost-todo

virtualenv venv
. venv/bin/activate

cd ghost-todo
./manage.py runserver

## DB

1. Create database
```sh
psql
```
```sql
CREATE DATABASE ghost_todo;

```
2. Migrate

```sh
python3 manage.py migrate
```
