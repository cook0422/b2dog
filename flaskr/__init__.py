
print(__name__)
import os
from flask import Flask,render_template,request
import random

app = Flask(__name__, instance_relative_config=True)
#app.config.from_object('websiteconfig')

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
    username = request.args.get('username')
    us = sei.query(AllOrder).filter(AllOrder.买家会员名==username).all()
    allcost = 0
    for i in us:
        allcost += i.打款商家金额
    print("该会员总消费：" + str(allcost))
    sei.close()
    db_session.remove()
    return "该会员总消费：" + str(allcost)

@app.route('/user/<string:username>')
def show_user_profile(username):
    sei = db_session()
    us = sei.query(AllOrder).filter(AllOrder.买家会员名==username).all()
    allcost = 0
    for i in us:
        allcost += i.打款商家金额
    print("该会员总消费：" + str(allcost))
    sei.close()
    db_session.remove()
    return username +" 总消费：" + str(allcost)

from flaskr.views import tests
app.register_blueprint(tests.bp)

'''set FLASK_APP=flaskr
set FLASK_ENV=development
flask run'''