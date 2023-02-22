# Gudlft
A Flask app to book competitions for clubs.

This project is a fork of [https://github.com/OpenClassrooms-Student-Center/Python_Testing](https://github.com/OpenClassrooms-Student-Center/Python_Testing)

It's all about testing the code : unit tests, integration tests, coverage tests and performance tests.


## Installation


### Clone this repository
``` 
git clone https://github.com/rhunold/projet11.git
```

### Create an environment at the root of the project
``` 
python3 -m venv env
```

### Activate the environment
``` 
python3 source env/bin/activate
```

### Install pip
``` 
python3 -m pip install 
```

### Install the requirements
``` 
pip install -r requirements.txt
```

## Database
We used json files to store informations about allowed users and competitions.

## Run server

After environment is launch, use this command line to start the server
```
python server.py
```

Server adress : [http://127.0.0.1:8000](http://127.0.0.1:8000)



## Test

### Pytest
Launch Pytest (unit tests and integration tests) and see every test results
```
pytest -v
```

### Coverage test
Launch Coverage tests and generate a html file
```
pytest --cov=. --cov-report html
```

### Performance tests
Because the server must be on during the test, you have to open a new terminal, reactivate the environnement if not activated, then go to the performance folder

```
cd tests/performance_tests/
```

Then lauch the command
```
locust
```

Then go to [http://0.0.0.0:8089 ](http://0.0.0.0:8089)

In the "Number of users" field, put 6.
In the "Host" field, put "http://127.0.0.1:8000"

When the "Status running" reach 6 users, you can click the stop Button to see results.

