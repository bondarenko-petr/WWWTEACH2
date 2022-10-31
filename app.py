from flask import Flask, render_template
import os

TEMPLATE_DIR = os.path.abspath('../templates')
STATIC_DIR = os.path.abspath('templates/images')

app = Flask(__name__, static_folder=STATIC_DIR)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
