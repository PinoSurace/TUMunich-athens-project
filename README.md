# Project Green

## How to install

If you want to run our app please make sure that you have installed python (version 3.5) and MySQL.

Go to the folder where you download our app and run these commands. It will create Python virtual environment for you.
It will also install python packages which are required for running our app. 

```python
python3.5 -m venv env
. env/bin/activate
python -m pip install -r src/requirements.txt
```

## How to run

Go to the `src` folder and run: 

```python
python app.py
```

Now you should be able to access our visualization on address `localhost:5000`

