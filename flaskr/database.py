from sqlalchemy import create_engine,Column, Integer, String, DateTime, \
     ForeignKey, event
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:Cook21!!@cook0422.mysql.rds.aliyuncs.com/taobao', convert_unicode=True，echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
#Base.metadata.create_all(bind=engine)

def init_db():
    # 在这里导入定义模型所需要的所有模块，这样它们就会正确的注册在
    # 元数据上。否则你就必须在调用 init_db() 之前导入它们。
   # import yourapplication.models
    Base.metadata.create_all(bind=engine)


class User(Base):
    __tablename__ = 'users'
    id = Column('user_id', Integer, primary_key=True)
    openid = Column('openid', String(200))
    name = Column(String(200))

    def __init__(self, name, openid):
        self.name = name
        self.openid = openid

    def to_json(self):
        return dict(name=self.name, is_admin=self.is_admin)

    @property
    def is_admin(self):
        return self.openid in app.config['ADMINS']

    def __eq__(self, other):
        return type(self) is type(other) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

class OpenIDUserNonce(Base):
    __tablename__ = 'openid_user_nonces'
    id = Column('user_nonce_id', Integer, primary_key=True)
    server_url = Column(String(1024))
    timestamp = Column(Integer)
    salt = Column(String(40))

#event.listen(db_session, 'after_flush', search.update_model_based_indexes)