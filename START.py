from flask import Flask
from flask import url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index page !'

@app.route('/hello')
def hello():
    return 'Hello page ! ' + url_for("projects")

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('hello'))
    print(url_for('hello', next='/'))
    print(url_for('show_subpath', subpath='JohnDoe'))

'''if __name__ == "__main__":
    app.run()
'''