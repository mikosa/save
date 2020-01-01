

docker run -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp -p 8000:8000 python:3 bash -c "python3 -m pip install Django && python3 -m pip install -r requirements.txt && python3 manage.py makemigrations sim && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000"

# Resemblance
measure similarity between two txt files (Python)

## Getting Started

Resemblance works on **Python 3+** and Django 2+.

Install dependencies:

```
python3 -m pip3 install -r requirements.txt
```
then run following commands:


```
python3 manage.py makemigrations sim
python3 manage.py migrate
python3 manage.py runserver
```
