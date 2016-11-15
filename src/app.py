from business import get_data_for_task_1
from flask import Flask, send_from_directory
from flask.json import jsonify
from flask_mysqldb import MySQL


app = Flask(__name__, static_url_path="")
app.config['DEBUG'] = True
mysql = MySQL(app)


@app.route('/')
def index():
    return send_from_directory("static", "index.html")


@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('static', path)


@app.route("/api/task1/<module_name>")
def task_1(module_name):
    data = get_data_for_task_1(module_name=module_name)
    return jsonify(result=data)


if __name__ == "__main__":
    app.run()
