from common.mysql_operate import db
from testcases.conftest import table_data


class SnowflakeReward:
    def common_snowflake_reward(self, activity_type, reward_type):
        sql = table_data["snowflake_reward_config"]["select_by_type"] % (activity_type, reward_type)
        data_id = db.select_db(sql)
        len_data = len(data_id)
        if reward_type.__eq__('1'):
            sql_item_sku = table_data["item_sku"]["select_by_item_id"] % 2260
            # sql_item_sku = "select id, name from item_sku where item_id = %s" % 2260
            data_sku_name = db.select_db(sql_item_sku)
            for i in range(len_data):
                sql = table_data["snowflake_reward_config"]["update_skuId_by_id"] \
                      % (data_sku_name[i]["id"], data_sku_name[i]["name"], data_id[i]["id"])
                db.execute_db(sql)
            return "更新成功"
        elif reward_type.__eq__('2'):
            sql_skill_card_info = table_data["skill_card_info"]["select_by_id"] % len_data
            data_skill_card_info = db.select_db(sql_skill_card_info)
            for i in range(len_data):
                sql = table_data["snowflake_reward_config"]["update_skillId_by_id"] \
                      % (data_skill_card_info[i]["id"], data_skill_card_info[i]["name"], data_id[i]["id"])
                db.execute_db(sql)
            return "更新成功"
        elif reward_type.__eq__('3'):
            sql_coupon_info = table_data["coupon_info"]["select_by_activity_id"] % len_data
            data_coupon_info = db.select_db(sql_coupon_info)
            for i in range(len_data):
                sql = table_data["snowflake_reward_config"]["update_couponId_by_id"] \
                      % (data_coupon_info[i]["id"], data_coupon_info[i]["name"], data_id[i]["id"])
                db.execute_db(sql)
            return "更新成功"

    def common_consumption_value(self, user_id, value, rest_num):
        sql = "update user_snowflake_consumption_value set total_value = %s,available_value=%s,snowflake_num=%s," \
              "snowflake_rest_num= %s where user_id= %s" % (value, value, rest_num, rest_num, user_id)
        db.execute_db(sql)
        return "更新成功"


snr = SnowflakeReward()
