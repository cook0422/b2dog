class Config(object):
    """配置参数"""
    #sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI="mysql://root:Cook21!!@cook0422.mysql.rds.aliyuncs.com/taobao"
    #设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    print("Config")
