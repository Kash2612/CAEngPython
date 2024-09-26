Step1:
```commandline
python3 -m venv venv
```
Step 2: ACTIVATE
``` 
source venv/bin/activate
```

Step 3:
```commandline
pip install flask
```

Step 4:
```commandline
```

Step 5: if main not defines:
```commandline
export FLASK_APP=app.py
export FLASK_END=development
flask run
```

otherwise:
```
python app.py
```

Step 6:
```commandline
pip install flask-SQLAlchemy
```