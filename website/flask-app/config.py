from os import urandom
# mysql数据库连接配置
dialect = 'mysql'
driver = 'pymysql'
username = 'root'
password = 'root'
host = 'localhost'
port = '3306'
database = 'ReaderClub'

SQLALCHEMY_DATABASE_URI = '''{dialect}+{driver}://{username}:{password}@{host}:
    {port}/{database}?charset=utf8'''.format(
    dialect=dialect, driver=driver, username=username,
    password=password, host=host, port=port, database=database)

SQLALCHEMY_TRACK_MODIFICATIONS = False

# 生成随机盐
SECRET_KEY = urandom(24)
