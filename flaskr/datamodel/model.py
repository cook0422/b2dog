# coding: utf-8
from sqlalchemy import Column, DateTime, Float, String, Table
from sqlalchemy.dialects.mysql import INTEGER
from flaskr.database import Base

class AllOrder(Base):
    __tablename__ = 'all_orders'

    订单编号 = Column(String(40), primary_key=True)
    买家会员名 = Column(String(80))
    买家支付宝账号 = Column(String(80))
    买家应付货款 = Column(Float)
    买家应付邮费 = Column(Float)
    买家支付积分 = Column(Float)
    总金额 = Column(Float)
    返点积分 = Column(Float)
    买家实际支付金额 = Column(Float)
    买家实际支付积分 = Column(Float)
    订单状态 = Column(String(30))
    买家留言 = Column(String(255))
    收货人姓名 = Column(String(60))
    收货地址 = Column(String(255))
    运送方式 = Column(String(30))
    联系电话 = Column(String(20))
    联系手机 = Column(String(20))
    订单创建时间 = Column(DateTime)
    订单付款时间 = Column(DateTime)
    宝贝标题 = Column(String(255))
    宝贝种类 = Column(String(10))
    物流单号 = Column(String(30))
    物流公司 = Column(String(30))
    订单备注 = Column(String(255))
    宝贝总数量 = Column(INTEGER(11))
    店铺Id = Column(String(30))
    店铺名称 = Column(String(60))
    确认收货时间 = Column(DateTime)
    打款商家金额 = Column(Float)

'''
class User(Base):
    __tablename__ = 'users'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
'''