
print(__name__)
import os
from flask import Flask,render_template
import random

app = Flask(__name__, instance_relative_config=True)
#app.config.from_object('websiteconfig')
app.run()

from flaskr.database import db_session
from flaskr.datamodel.orders_mdl import User
from flaskr.datamodel.model import AllOrder

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
    '''
    u = User('newy----ear','------@localhost')
    sei = db_session()
    sei.add(u)
    sei.commit()'''
    sei = db_session()
    us = sei.query(AllOrder).filter(AllOrder.买家会员名=='最爱雷宝宝').all()
    for i in us:
        print(i.打款商家金额)
    sei.close()
    db_session.remove()
    return 'Welcome to my data-world !'


from flaskr.views import tests
app.register_blueprint(tests.bp)