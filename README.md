#### Simple Prefix/Infix Calculator

----

##### How to run
    1. Install requirements in `requirements.txt`
    2. Start Django using `python manage.py runserver`
    3. Access web interface on `localhost:8000`

##### How to run test suite
    1. Install requirements in `requirements.txt`
    2. Run `pytest`
    
##### How to use API
Access API from `localost:8000/api` after starting Django server.

###### Prefix notation
```json
Request:
POST /api {"expression":  "+ 1 2"}

Response:
{
  "expression": "+ 1 2",
  "result": 3
}
```

###### Infix notation
```json
Request:
POST /api?infix=true {"expression":  "1 + 2"}

Response:
{
  "expression": "1 + 2",
  "result": 3
}
```

##### Test output
```
======================================================================================================================================================================= test session starts ========================================================================================================================================================================
platform win32 -- Python 3.7.7, pytest-6.2.1, py-1.10.0, pluggy-0.13.1
rootdir: C:*\sww, configfile: pytest.ini, testpaths: ./tests
plugins: django-3.8.0
collected 18 items                                                                                                                                                                                                                                                                                                                                                  

tests\test_api.py ...
tests\test_lib.py ...............

================================================================================================================================================================== 18 passed in 0.26s ===================================================================================================================================================================
```