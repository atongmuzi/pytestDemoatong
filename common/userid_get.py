from common.mysql_operate import db
from common.logger import logger


class UserIdGet:
    def userid_get(self, **kwargs):
        phone = dict(**kwargs).get("phone")
        nickname = dict(**kwargs).get("nickname")
        if phone is not None:
            select_sql = "select id from user where phone = '%s'" % phone
            data = db.select_db(select_sql)
            return data[0]["id"]
        else:
            select_sql = "select id from user where nickname = '%s' order by id desc limit 1" % nickname
            data = db.select_db(select_sql)
            return data[0]["id"]

    def delete_record(self, tablename, user_id=None, phone=None, nickname=None):
        if user_id is None:
            user_id = ug.userid_get(phone=phone, nickname=nickname)
        delete_sql = "delete from %s where user_id = '%s' " % (tablename, user_id)
        db.execute_db(delete_sql)


ug = UserIdGet()

if __name__ == '__main__':
    ug.delete_record('user_snowflake_boost_log', user_id='1645')
    logger.info("删除成功")
