import os
# dbtype+driver://username:password@host:port/database
class DBConfig():
	"""
	一个和数据库连接参数相关的类
	"""
	__DBTYPE = 'mysql'
	__DRIVER = 'mysqldb'
	__USERNAME = 'root'
	__PASSWORD = 'lilei120400'
	__HOST = '127.0.0.1'
	__PORT = '3306'
	__DATABASE = 'project_test'
	# 获取DB_URI的方法
	def db_uri(self):
		DB_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(self.__DBTYPE, self.__DRIVER, self.__USERNAME,
		 self.__PASSWORD, self.__HOST, self.__PORT, self.__DATABASE)
		return DB_URI

db_config = DBConfig()
DB_URI = db_config.db_uri()
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.urandom(24)