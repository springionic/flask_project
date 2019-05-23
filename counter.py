"""
计数器
"""
from extends import db

def counter(q):
    """
    计数器，每当点击问题，执行 counter +1
    :param q: 查询出的一条数据question
    :return:
    """
    try:
        q.counter += 1
        db.session.commit()
    except:
        db.session.rollback()