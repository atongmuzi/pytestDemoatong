from testcases.conftest import base_data
from common.authorization_get import au


class Headers:

    def test_headers_get(self):
        user_id = base_data["init_user"]["user_id"]
        v_Authorization = au.test_authorization_get(user_id, 1, channel_type=2)
        headers = {
            "Authorization": v_Authorization
        }
        return headers

    def test_headers_get_admin(self):
        user_id = base_data["init_user"]["admin_user_id"]
        v_Authorization = au.test_authorization_get(user_id, 2)
        headers = {
            "Authorization": v_Authorization
        }
        return headers


headers = Headers()

