import os
from flask import Flask,render_template


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('websiteconfig')


@app.errorhandler(404)
def not_found(error):
    return "404"

# a simple page that says hello
@app.route('/')
def index():
    return 'Welcome to my data-world !'

from flaskr.views import tests
app.register_blueprint(tests.bp)