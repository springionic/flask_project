from extends import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Users(db.Model):
	# 用户表/users
	__tablename__ = 'users'
	s_id = db.Column(db.Integer, primary_key=True)  # 学号
	username = db.Column(db.String(32), nullable=False)  # 用户名
	password = db.Column(db.String(128), nullable=False)  # 密码
	power = db.Column(db.SmallInteger, default=0, nullable=False)  # 权限
	# 初始化函数（构造函数）
	def __init__(self, *args, **kwargs):
		s_id = kwargs.get('s_id')
		username = kwargs.get('username')
		password = kwargs.get('password')
		self.s_id = s_id
		self.username = username
		self.password = generate_password_hash(password)
	# 与构造函数配合，实现对密码的加密与解密
	def check_password(self, raw_password):
		result = check_password_hash(self.password, raw_password)
		return result

	def __str__(self):
		return self.username


class CarpoolQuestions(db.Model):
	# 拼车发布表/carpool_questions
	__tablename__ = 'carpool_questions'
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)  # 序号
	s_id = db.Column(db.Integer, db.ForeignKey('users.s_id'))  # 外键学生学号
	title = db.Column(db.String(64), nullable=False)  # 标题
	time = db.Column(db.String(64), nullable=False)  # 发布时间
	destination = db.Column(db.String(64), nullable=False)  # 目的地
	num = db.Column(db.String(16), nullable=False)  # 拼车人数
	contact = db.Column(db.String(32), nullable=False)  # 联系方式
	detail = db.Column(db.Text)  # 详情描述
	# now() 获取的是服务器第一次运行的时间
	# now  获取的是 每次创建一个模型的时候，都获取当前的时间， 这里用datetime.now
	create_time = db.Column(db.DATETIME, default=datetime.now)  # 此消息创建时间
	author = db.relationship('Users', backref = db.backref('carpool_questions'))  # 获取拼车问题的作者，反向是帖子


class CarpoolAnswers(db.Model):
	# 拼车评论表/carpool_answers
	__tablename__ = 'carpool_answers'
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)  # 序号
	s_id = db.Column(db.Integer, db.ForeignKey('users.s_id'))  # 外键学生学号
	question_id = db.Column(db.Integer, db.ForeignKey('carpool_questions.id'))  # 外键问题序号
	content = db.Column(db.Text, nullable=False)  # 评论内容
	create_time = db.Column(db.DATETIME, default=datetime.now)  # 此评论的创建时间
	carpool_question = db.relationship('CarpoolQuestions', backref = db.backref('carpool_answers', order_by=id.desc()))
	author = db.relationship('Users')  # 获取评论的作者


class PlayQuestions(db.Model):
	# 约吧发布表/play_questions
	__tablename__ = 'play_questions'
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)  # 序号
	s_id = db.Column(db.Integer, db.ForeignKey('users.s_id'))  #外键学生学号
	title = db.Column(db.String(64), nullable=False)  #活动主题
	time = db.Column(db.String(64), nullable=False)  # 时间
	location = db.Column(db.String(64), nullable=False)  # 地点
	contact = db.Column(db.String(32), nullable=False)  # 联系方式
	detail = db.Column(db.Text)  # 活动详情
	create_time = db.Column(db.DATETIME, default=datetime.now)  # 创建时间
	author = db.relationship('Users', backref=db.backref('play_questions'))  # 获取约吧问题的作者，反向为帖子


class PlayAnswers(db.Model):
	# 约吧评论表/play_answers
	__tablename__ = 'play_answers'
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)  # 序号
	s_id = db.Column(db.Integer, db.ForeignKey('users.s_id'))  # 外键学生学号
	question_id = db.Column(db.Integer, db.ForeignKey('play_questions.id'))  # 外键问题序号
	content = db.Column(db.Text, nullable=False)  # 评论内容
	create_time = db.Column(db.DATETIME, default=datetime.now)  # 评论创建时间
	play_question = db.relationship('PlayQuestions', backref=db.backref('play_answers', order_by=id.desc()))
	author = db.relationship('Users')  # 获取评论的作者


class SearchQuestions(db.Model):
	# 寻物启事表/search_questions
	__tablename__ = 'search_questions'
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)  #序号
	s_id = db.Column(db.Integer, db.ForeignKey('users.s_id'))  # 外键学生学号
	title = db.Column(db.String(64), nullable=False)  # 标题
	time = db.Column(db.String(64), nullable=False)  # 丢失时间
	location = db.Column(db.String(64), nullable=False)  # 丢失地点
	contact = db.Column(db.String(32), nullable=False)  # 联系方式
	detail = db.Column(db.Text)  # 详情描述
	picture = db.Column(db.String(128))  # 图片链接
	create_time = db.Column(db.DATETIME, default=datetime.now)  # 创建时间
	author = db.relationship('Users', backref=db.backref('search_questions'))  # 获取寻物启事的作者，反向是帖子


class SearchAnswers(db.Model):
	# 寻物评论表/search_answers
	__tablename__ = 'search_answers'
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)  # 序号
	s_id = db.Column(db.Integer, db.ForeignKey('users.s_id'))  # 外键学生学号
	question_id = db.Column(db.Integer, db.ForeignKey('search_questions.id'))  # 外键问题号
	content = db.Column(db.Text, nullable=False)  # 评论内容
	create_time = db.Column(db.DATETIME, default=datetime.now)  # 评论创建时间
	search_question = db.relationship('SearchQuestions', backref=db.backref('search_answers', order_by=id.desc()))
	author = db.relationship('Users')  # 获取评论的作者


class LostQuestions(db.Model):
	# 失物招领表/lost_questions
	__tablename = 'lost_questions'
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)  # 序号
	s_id = db.Column(db.Integer, db.ForeignKey('users.s_id'))  # 外键学生学号
	title = db.Column(db.String(64), nullable=False)  # 标题
	time = db.Column(db.String(64), nullable=False)  # 拾取时间
	location = db.Column(db.String(64), nullable=False)  # 拾取地点
	contact = db.Column(db.String(32), nullable=False)  # 联系方式
	detail = db.Column(db.Text)  # 详情描述
	picture = db.Column(db.String(128))  # 图片链接
	create_time = db.Column(db.DATETIME, default=datetime.now)  # 创建时间
	author = db.relationship('Users', backref=db.backref('lost_questions'))  # 获取失物招领的作者，反向是帖子


class LostAnswers(db.Model):
	# 失物评论表/lost_answers
	__tablename__ = 'lost_answers'
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)  # 序号
	s_id = db.Column(db.Integer, db.ForeignKey('users.s_id'))  # 外键
	question_id = db.Column(db.Integer, db.ForeignKey('lost_questions.id'))  # 外键
	content = db.Column(db.Text, nullable=False)  # 评论内容
	create_time = db.Column(db.DATETIME, default=datetime.now)  # 评论创建时间
	lost_question = db.relationship('LostQuestions', backref=db.backref('lost_answers', order_by=id.desc()))
	author = db.relationship('Users')  # 获取评论的作者


class RightPart(db.Model):
	# 右侧部分
	__tablename__ = 'right_part'
	id = db.Column(db.Integer, autoincrement=True, primary_key=True)  # 序号
	event = db.Column(db.String(64))
	activity = db.Column(db.String(64))
	interest = db.Column(db.String(64))








