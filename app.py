from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import g
from extends import db
import config
from models import Users
from models import CarpoolQuestions
from models import CarpoolAnswers
from models import PlayQuestions
from models import PlayAnswers
from models import SearchQuestions
from models import SearchAnswers
from models import LostQuestions
from models import LostAnswers
from sqlalchemy import or_
from werkzeug.utils import secure_filename
from datetime import datetime
from login_limit import login_required
import os



app = Flask(__name__)
db.init_app(app)
app.config.from_object(config)


# 用户登录路由
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        student_id = request.form.get('student_id')
        password = request.form.get('password')
        code = request.form.get('code')
        page_code = request.form.get('page_code')
        user = Users.query.filter(Users.s_id == student_id).first()
        if code.lower() == page_code.lower():
            if user and user.check_password(password):
                session['student_id'] = user.s_id
                return redirect(url_for('index'))
            else:
                return '''<br><br><br><br><br><br><hr><center><h1>
                        用户名或密码错误，请返回重试！</h1></center><hr>'''
        else:
            return '''<br><br><br><br><br><br><hr><center><h1>
                    验证码输入有误，请返回重试！</h1></center><hr>'''


# 用户注册路由
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        student_id = request.form.get('student_id')
        username = request.form.get('username')
        password = request.form.get('password')
        code = request.form.get('code')
        page_code = request.form.get('page_code')
        # this_code = request.json['this_code']
        # print(this_code)
        user = Users.query.filter(Users.s_id == student_id).first()
        if code.lower() == page_code.lower():
            if user:
                return '''<br><br><br><br><br><br><hr><center><h1>
                        该用户已经注册，请返回重新注册！</h1></center><hr>'''
            else:
                try:
                    user = Users(s_id=student_id, username=username, password=password)
                    db.session.add(user)
                    db.session.commit()
                    return redirect(url_for('login'))
                except:
                    db.session.rollback()
                    return redirect(url_for('register'))
        else:
            return '''<br><br><br><br><br><br><hr><center><h1>
                    验证码输入有误，请返回重试！</h1></center><hr>'''


# 用户注销的路由
@app.route('/logout')
@login_required
def logout():
    del session['student_id']
    return redirect(url_for('login'))


# 用户个人信息的路由
@app.route('/user_information')
@login_required
def user_information():
    return render_template('personal_information.html')


# 主页路由
@app.route('/')
def index():
    return render_template('index.html')


# 打车拼车页路由
@app.route('/carpool')
def carpool():
    page = request.args.get('page', 1, type=int)
    questions = CarpoolQuestions.query.order_by(db.desc(CarpoolQuestions.create_time)).paginate(page=page, per_page=3)
    prev_page = questions.prev_num  # 返回上一页的页码
    next_page = questions.next_num  # 返回下一页的页码
    curr_page = questions.page      # 返回当前页的页码
    num_list = questions.pages      # 显示总的分页数
    questions = questions.items     # 返回当前页面中所有记录

    content = {
        'questions': questions,
        'num_list': range(1, num_list+1),
        'prev_page': prev_page,
        'next_page': next_page,
        'curr_page': curr_page
    }

    return render_template('carpool.html', **content)


# 打车拼车发布页路由
@app.route('/carpool_release', methods=['GET', 'POST'])
@login_required
def carpool_release():
    if request.method == 'GET':
        return render_template('carpool_release.html')
    else:
        try:
            title = request.form.get('title')
            time = request.form.get('time')
            destination = request.form.get('destination')
            num = request.form.get('num')
            contact = request.form.get('contact')
            detail = request.form.get('detail')
            question = CarpoolQuestions(
                title=title, time=time, destination=destination, num=num, contact=contact, detail=detail
            )
            question.author = g.user
            db.session.add(question)
            db.session.commit()
            return redirect(url_for('carpool'))
        except:
            db.session.rollback()
            return redirect(url_for('carpool_release'))


# 打车拼车详情页路由
@app.route('/carpool_text/<question_id>')
def carpool_text(question_id):
    question_content = CarpoolQuestions.query.filter(CarpoolQuestions.id == question_id).first()
    return render_template('carpool_text.html', question_content=question_content)


# 拼车问题评论路由
@app.route('/carpool_answer', methods=['POST'])
@login_required
def carpool_answer():
    content = request.form.get('answer')
    question_id = request.form.get('question_id')
    answer = CarpoolAnswers(content=content)
    answer.author = g.user
    question = CarpoolQuestions.query.filter(CarpoolQuestions.id == question_id).first()
    answer.carpool_question = question
    try:
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for('carpool_text', question_id=question_id))
    except:
        db.session.rollback()
        return redirect(url_for('carpool_text', question_id=question_id))


# 拼车搜索路由
@app.route('/carpool_search')
def carpool_search():
    search = request.args.get('search')
    questions = CarpoolQuestions.query.filter(or_(CarpoolQuestions.title.contains(search),
                                                  CarpoolQuestions.detail.contains(search))).order_by(db.desc(CarpoolQuestions.create_time))
    return render_template('carpool.html', questions=questions)


# 约吧页路由
@app.route('/data')
def data():
    page = request.args.get('page', 1, type=int)
    questions = PlayQuestions.query.order_by(db.desc(PlayQuestions.create_time)).paginate(page=page, per_page=3)
    prev_page = questions.prev_num  # 返回上一页的页码
    next_page = questions.next_num  # 返回下一页的页码
    curr_page = questions.page  # 返回当前页的页码
    num_list = questions.pages  # 显示总的分页数
    questions = questions.items  # 返回当前页面中所有记录

    content = {
        'questions': questions,
        'num_list': range(1, num_list+1),
        'curr_page': curr_page,
        'prev_page': prev_page,
        'next_page': next_page
    }
    return render_template('data.html', **content)


# 约吧发布页路由
@app.route('/data_release', methods=['GET', 'POST'])
@login_required
def data_release():
    if request.method == 'GET':
        return render_template('data_release.html')
    else:
        try:
            title = request.form.get('title')
            time = request.form.get('time')
            location = request.form.get('location')
            contact = request.form.get('contact')
            detail = request.form.get('detail')
            question = PlayQuestions(
                title=title, time=time, location=location, contact=contact, detail=detail
            )
            question.author = g.user
            db.session.add(question)
            db.session.commit()
            return redirect(url_for('data'))
        except:
            db.session.rollback()
            return redirect(url_for('data_release'))


# 约吧详情页路由
@app.route('/data_text/<question_id>')
def data_text(question_id):
    question_content = PlayQuestions.query.filter(PlayQuestions.id == question_id).first()
    return render_template('data_text.html', question_content=question_content)


# 约吧评论路由
@app.route('/data_answer', methods=['POST'])
@login_required
def data_answer():
    content = request.form.get('content')
    question_id = request.form.get('question_id')
    answer = PlayAnswers(content=content)
    answer.author = g.user
    question = PlayQuestions.query.filter(PlayQuestions.id == question_id).first()
    answer.play_question = question
    try:
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for('data_text', question_id=question_id))
    except:
        db.session.rollback()
        return redirect(url_for('data_text', question_id=question_id))


# 约吧搜索路由
@app.route('/data_search')
def data_search():
    search = request.args.get('search')
    questions = PlayQuestions.query.filter(or_(PlayQuestions.title.contains(search),
                                               PlayQuestions.detail.contains(search))).order_by(db.desc(PlayQuestions.create_time))
    return render_template('data.html', questions=questions)


# 失物招领页面路由
@app.route('/loststandfind')
def loststandfind():
    activate = request.args.get('activate', 0, int)
    page_a = request.args.get('page_a', 1, int)
    page_b = request.args.get('page_b', 1, int)
    q_a = LostQuestions.query.order_by(db.desc(LostQuestions.create_time)).paginate(page=page_a, per_page=6)
    q_b = SearchQuestions.query.order_by(db.desc(SearchQuestions.create_time)).paginate(page=page_b, per_page=6)
    a_prev_page = q_a.prev_num  # 返回上一页的页码
    a_next_page = q_a.next_num  # 返回下一页的页码
    a_curr_page = q_a.page  # 返回当前页的页码
    a_num_list = q_a.pages  # 显示总的分页数
    a_questions = q_a.items  # 返回当前页面中所有记录

    b_prev_page = q_b.prev_num  # 返回上一页的页码
    b_next_page = q_b.next_num  # 返回下一页的页码
    b_curr_page = q_b.page  # 返回当前页的页码
    b_num_list = q_b.pages  # 显示总的分页数
    b_questions = q_b.items  # 返回当前页面中所有记录


    questions_a = list(a_questions)
    questions_b = list(b_questions)
    n = 3
    # 把查询结果三三分成一个列表，然后再存入一个列表中（列表的推导式）
    questions_a = [questions_a[i:i + n] for i in range(0, len(questions_a), n)]
    questions_b = [questions_b[i:i + n] for i in range(0, len(questions_b), n)]

    content = {
        'questions_a': questions_a,
        'a_num_list': range(1, a_num_list+1),
        'a_curr_page': a_curr_page,
        'a_prev_page': a_prev_page,
        'a_next_page': a_next_page,
        ##############################################
        'questions_b': questions_b,
        'b_num_list': range(1, b_num_list+1),
        'b_curr_page': b_curr_page,
        'b_prev_page': b_prev_page,
        'b_next_page': b_next_page,
        ##############################################
        'act': activate
    }
    return render_template('lostandfind.html', **content)


# 失物招领发布路由
@app.route('/find_release', methods=['GET', 'POST'])
@login_required
def find_release():
    if request.method == 'GET':
        return render_template('find_release.html')
    else:
        title = request.form.get('title')
        time = request.form.get('time')
        location = request.form.get('location')
        contact = request.form.get('contact')
        detail = request.form.get('detail')
        try:
            picture = request.files['pclog']
            base_path = os.path.dirname(__file__)  # 当前文件所在路径
            # 把原图片的名字以点分割，然后end为其后缀名
            s = str(picture.filename).split('.')
            end = s[len(s) - 1]
            filename = str(datetime.now()) + '.' + end  # 保存的图片名字
            # 将图片保存到 static/pictures 文件夹中，并以 filename 命名
            upload_path = os.path.join(base_path, 'static/pictures', secure_filename(filename))
            picture.save(upload_path)
            #####################################################################################
            question = LostQuestions(title=title, time=time, location=location, contact=contact,
                                     detail=detail, picture=secure_filename(filename))
            question.author = g.user
            try:
                db.session.add(question)
                db.session.commit()
                return redirect(url_for('loststandfind'))
            except:
                db.session.rollback()
                return redirect(url_for('find_release'))
        except:
            question = LostQuestions(title=title, time=time, location=location, contact=contact, detail=detail)
            question.author = g.user
            try:
                db.session.add(question)
                db.session.commit()
                return redirect(url_for('loststandfind'))
            except:
                db.session.rollback()
                return redirect(url_for('find_release'))


# 失物招领详情页路由
@app.route('/find_text/<question_id>')
def find_text(question_id):
    question_content = LostQuestions.query.filter(LostQuestions.id==question_id).first()
    return render_template('find_text.html', question_content=question_content)


# 失物招领评论路由
@app.route('/find_answer', methods=['POST'])
@login_required
def find_answer():
    content = request.form.get('content')
    question_id = request.form.get('question_id')
    answer = LostAnswers(content=content)
    answer.author = g.user
    question = LostQuestions.query.filter(LostQuestions.id==question_id).first()
    answer.lost_question = question
    try:
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for('find_text', question_id=question_id))
    except:
        db.session.rollback()
        return redirect(url_for('find_text', question_id=question_id))


# 寻物启事发布路由
@app.route('/lost_release', methods=['GET', 'POST'])
@login_required
def lost_release():
    if request.method == 'GET':
        return render_template('lost_release.html')
    else:
        title = request.form.get('title')
        time = request.form.get('time')
        location = request.form.get('location')
        contact = request.form.get('contact')
        detail = request.form.get('detail')
        try:
            picture = request.files['pclog']
            base_path = os.path.dirname(__file__)  # 当前文件所在路径
            # 把原图片的名字以点分割，然后end为其后缀名
            s = str(picture.filename).split('.')
            end = s[len(s) - 1]
            filename = str(datetime.now()) + '.' + end  # 保存的图片名字
            # 将图片保存到 static/pictures 文件夹中，并以 filename 命名
            upload_path = os.path.join(base_path, 'static/pictures', secure_filename(filename))
            picture.save(upload_path)
            #####################################################################################
            question = SearchQuestions(title=title, time=time, location=location, contact=contact,
                                     detail=detail, picture=secure_filename(filename))
            question.author = g.user
            try:
                db.session.add(question)
                db.session.commit()
                return redirect(url_for('loststandfind'))
            except:
                db.session.rollback()
                return redirect(url_for('lost_release'))
        except:
            question = SearchQuestions(title=title, time=time, location=location, contact=contact, detail=detail)
            question.author = g.user
            try:
                db.session.add(question)
                db.session.commit()
                return redirect(url_for('loststandfind'))
            except:
                db.session.rollback()
                return redirect(url_for('lost_release'))


# 寻物启事详情页路由
@app.route('/lost_text/<question_id>')
def lost_text(question_id):
    question_content = SearchQuestions.query.filter(SearchQuestions.id==question_id).first()
    return render_template('lost_text.html', question_content=question_content)


# 寻物启事评论路由
@app.route('/lost_answer', methods=['POST'])
@login_required
def lost_answer():
    content = request.form.get('content')
    question_id = request.form.get('question_id')
    answer = SearchAnswers(content=content)
    answer.author = g.user
    question = SearchQuestions.query.filter(SearchQuestions.id==question_id).first()
    answer.search_question = question
    try:
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for('lost_text', question_id=question_id))
    except:
        db.session.rollback()
        return redirect(url_for('lost_text', question_id=question_id))


# 失物寻物搜索路由
@app.route('/lost_find_search')
def lost_find_search():
    search = request.args.get('search')
    questions_a = LostQuestions.query.filter(or_(LostQuestions.title.contains(search),
                                                      LostQuestions.detail.contains(search))).order_by(db.desc(LostQuestions.create_time))
    questions_b = SearchQuestions.query.filter(or_(SearchQuestions.title.contains(search),
                                                       SearchQuestions.detail.contains(search))).order_by(db.desc(SearchQuestions.create_time))
    questions_a = list(questions_a)
    questions_b = list(questions_b)
    n = 3
    questions_a = [questions_a[i:i+n] for i in range(0, len(questions_a), n)]
    questions_b = [questions_b[i:i+n] for i in range(0, len(questions_b), n)]
    return render_template('lostandfind.html', questions_a=questions_a, questions_b=questions_b)


# 在用户发送的请求之前执行的函数，钩子函数
@app.before_request
def my_before_request():
    student_id = session.get('student_id')
    if student_id:
        user = Users.query.filter(Users.s_id == student_id).first()
        if user:
            g.user = user


# 在用户请求之后执行的函数
# 此函数的返回值在所有页面都可用，上下文处理器
@app.context_processor
def my_context_processor():
    if hasattr(g, 'user'):
        return {'user': g.user}
    return {}



# 后台管理模块，写在最后
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, BaseView, expose, AdminIndexView


admin = Admin(app, name='后台管理系统', index_view=AdminIndexView(
        template='admin.html'
    ))

admin.add_view(ModelView(Users, db.session, name=u'用户管理'))
admin.add_view(ModelView(CarpoolQuestions, db.session, name=u'拼车发布管理'))
admin.add_view(ModelView(CarpoolAnswers, db.session, name=u'拼车评论管理'))
admin.add_view(ModelView(PlayQuestions, db.session, name=u'约吧发布管理'))
admin.add_view(ModelView(PlayAnswers, db.session, name=u'约吧评论管理'))
admin.add_view(ModelView(SearchQuestions, db.session, name=u'寻物发布管理'))
admin.add_view(ModelView(SearchAnswers, db.session, name=u'寻物评论管理'))
admin.add_view(ModelView(LostQuestions, db.session, name=u'失物招领管理'))
admin.add_view(ModelView(LostAnswers, db.session, name=u'失物招领评论管理'))




if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='8000')
