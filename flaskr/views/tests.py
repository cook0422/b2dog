import sys
from flask import Flask,render_template,Blueprint
from flask import url_for
from jinja2 import Markup, Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from .import echartsT



bp = Blueprint('auth', __name__, url_prefix='/')

@bp.route('/inds')
def inds():
    return render_template("index.html")
    #return Markup(echartsT.Makebar().render_embed())

@bp.route('/hello')
def hello():
    return 'Hello page ! ' + url_for("projects")

@bp.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@bp.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@bp.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath

@bp.route('/projects/')
def projects():
    return 'The project page'

@bp.route('/about')
def about():
    return 'The about page'

'''with bp.test_request_context():
    print(url_for('index'))
    print(url_for('hello'))
    print(url_for('hello', next='/'))
    print(url_for('show_subpath', subpath='JohnDoe'))'''

@bp.route("/barChart")
def get_bar_chart():
    c = echartsT.line3d_base()
    return c.dump_options()

