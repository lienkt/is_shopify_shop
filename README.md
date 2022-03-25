

Download Python 3.10.4
https://www.python.org/downloads/

What Python version can I use with Django?
Django version (4.0 ) -	Python versions (3.8, 3.9, 3.10)
         	
Install Django by:
### `python -m pip install Django`

### `pip install djangorestframework`
### `pip install requests`
### `pip install numpy`

Getting project from Github and run project by:

### `python manage.py runserver`

# Exercise 1: is_shopify_shop

http://127.0.0.1:8000/api/is_shopify_shop/?url=https://www.respire.co/
=>true
http://127.0.0.1:8000/api/is_shopify_shop/?url=https://www.perus.co/
=>true
http://127.0.0.1:8000/api/is_shopify_shop/?url=https://www.joone.fr/
=>true
http://127.0.0.1:8000/api/is_shopify_shop/?url=https://www.nocibe.fr/
=>false

# Exercise 2: first missing positive
http://127.0.0.1:8000/api/first_missing_positive/?array=[-1,2,3]
=>1
http://127.0.0.1:8000/api/first_missing_positive/?array=[1, 2, 0]
=>3
http://127.0.0.1:8000/api/first_missing_positive/?array=[3, 4, -1, 1]
=>2
http://127.0.0.1:8000/api/first_missing_positive/?array=[-3,2,3,4,5,6,6,1]
=>7
