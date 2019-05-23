from flask import Blueprint
from flask import request
from flask import jsonify

from extends import db
from models import Users
from models import CarpoolQuestions
from models import PlayQuestions
from models import LostQuestions
from models import SearchQuestions


ajax = Blueprint('ajax', __name__)


# 修改用户昵称的路由
@ajax.route('/rename', methods=['POST'])
def rename():
    new_name = request.form.get('new_name')
    user_id = int(request.form.get('user_id'))
    user = Users.query.filter(Users.s_id == user_id).first()
    # 给前端返回json数据，status值为1，成功，0，失败
    if not new_name:
        return jsonify({'status': 0})
    try:
        user.username = new_name
        db.session.commit()
        return jsonify({'status': 1})
    except:
        db.session.rollback()
        return jsonify({'status': 0})

# 删除拼车记录的路由
@ajax.route('/del_carpool', methods=['POST'])
def del_carpool():
    carpool_id = int(request.form.get('carpool_id'))
    carpool_question = CarpoolQuestions.query.get(carpool_id)
    if not carpool_question:
        return jsonify({'status': 0})
    try:
        db.session.delete(carpool_question)
        db.session.commit()
        return jsonify({'status': 1})
    except:
        db.session.rollback()
        return jsonify({'status': 0})

# 删除约吧记录的路由
@ajax.route('/del_play', methods=['POST'])
def del_play():
    play_id = int(request.form.get('play_id'))
    play_question = PlayQuestions.query.get(play_id)
    if not play_question:
        return jsonify({'status': 0})
    try:
        db.session.delete(play_question)
        db.session.commit()
        return jsonify({'status': 1})
    except:
        db.session.rollback()
        return jsonify({'status': 0})

# 删除寻物启事的路由
@ajax.route('/del_search', methods=['POST'])
def del_search():
    search_id = int(request.form.get('search_id'))
    search_question = SearchQuestions.query.get(search_id)
    if not search_question:
        return jsonify({'status': 0})
    try:
        db.session.delete(search_question)
        db.session.commit()
        return jsonify({'status': 1})
    except:
        db.session.rollback()
        return jsonify({'status': 0})

# 删除失物招领记录的路由
@ajax.route('/del_lost', methods=['POST'])
def del_lost():
    lost_id = int(request.form.get('lost_id'))
    lost_question = LostQuestions.query.get(lost_id)
    if not lost_question:
        return jsonify({'status': 0})
    try:
        db.session.delete(lost_question)
        db.session.commit()
        return jsonify({'status': 1})
    except:
        db.session.rollback()
        return jsonify({'status': 0})





