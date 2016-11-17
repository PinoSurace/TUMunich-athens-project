from business import get_data_for_task_1, get_curriculum, get_data_for_task_2, get_data_for_task_3
from flask import Flask, send_from_directory
from flask.json import jsonify

app = Flask(__name__, static_url_path="")
app.config['DEBUG'] = True


@app.route('/')
def index():
    return send_from_directory("static", "index.html")


@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('static', path)


@app.route("/api/curriculum")
def curriculum():
    data = get_curriculum()
    return jsonify(result=data)


@app.route("/api/task1/<curriculum_code>")
def task_1(curriculum_code):
    data = get_data_for_task_1(curriculum_code=curriculum_code)
    return jsonify(result=data)


@app.route("/api/task2/<curriculum_code>")
def task_2(curriculum_code):
    data = get_data_for_task_2(curriculum_code=curriculum_code)
    return jsonify(result=data)


@app.route("/api/task3")
def task_3():
    data = get_data_for_task_3()
    return jsonify(result=data)


if __name__ == "__main__":
    app.run()
