# Project Green

## How to install

### Step 1

If you want to run our app please make sure that you have installed python (version 3.5) and MySQL.

Go to the source folder (`src`) and run these commands. It will create Python virtual environment for you.
It will also install python packages which are required for running our app. 

```bash
$ python3.5 -m venv env
$ . env/bin/activate
$ python -m pip install -r src/requirements.txt
```

### Step 2
You have to create `src/config.cfg` file where you have to put mainly information about your database. You can use our example of config located in `src/config.cfg.example`.

### Step 3
In order for the program to display the data rapidly, we had to preprocess the data and store it in new tables. For that you just need to go to the `src` folder and run this command:

```bash
$ python preprocessor.py
```

### Step 4
Now we have to install libraries for `javascript` part. You need to have `bower` in your computer (see installation guide - https://bower.io).
Once you have it you can just run this command in folder `src/static/`:

```bash
$ bower install
```

## How to run

Then you can just start the app: 

```bash
$ python app.py
```

Now you should be able to access our visualisation on address `localhost:5000`

