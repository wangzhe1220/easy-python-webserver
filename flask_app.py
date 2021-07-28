from flask import Flask, send_from_directory, jsonify, request, Response
from flask_cors import CORS
from flask_executor import Executor

app = Flask(__name__)
CORS(app)
executor = Executor()
executor.init_app(app)


# application/json
@app.route('/json')
def application_json():
    hello = {"hello": "world"}
    return jsonify(hello)


# text/html
@app.route('/text')
def text():
    hello = 'hello world'
    return hello


# image/png
@app.route('/image')
def image():
    with open('resource/flask-logo.png', 'rb') as f:
        img = f.read()
    return Response(img, mimetype='image/png')


if __name__ == '__main__':
    app.run(
        # allow all IP access
        host='0.0.0.0',
        # run on port 9000
        port=9000
    )
