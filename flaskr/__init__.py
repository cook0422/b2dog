
print(__name__)
import os
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__, instance_relative_config=True)
#app.config.from_object('websiteconfig')


@app.route('/initdb')
def initdb(error):
    from flaskr.database import init_db
    init_db()
    return "db done"

@app.errorhandler(404)
def not_found(error):
    return "404"

# a simple page that says hello
@app.route('/')
def index():
    from flaskr.database import db_session
    from flaskr.datamodel.orders_mdl import User
    from flaskr.datamodel.model import AllOrder
    u = User('564687','2323@localhost')
    sei = db_session()
    sei.add(u)
    sei.commit()
    us = sei.query(AllOrder).filter(AllOrder.买家会员名=='最爱雷宝宝').one()
    print(us.买家会员名)
    sei.close()
    return 'Welcome to my data-world !'


from flaskr.views import tests
app.register_blueprint(tests.bp)