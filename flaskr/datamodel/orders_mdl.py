
from sqlalchemy import Column, Integer, String
from flaskr.database import Base
# pip 安装sqlacodegen神器 生成数据库对象
# sqlacodegen mysql+pymysql://root:Cook21!!@cook0422.mysql.rds.aliyuncs.com/taobao --outfile d:\model.py

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)

