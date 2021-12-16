from testcases.conftest import base_data
from common.authorization_get import au
from enumc.platform import Platform


class Headers:

    def test_headers_get(self):
        """
        小程序端,platform_type= 1
        """
        user_id = base_data["init_user"]["user_id"]
        v_Authorization = au.test_authorization_get(user_id, Platform.mini_program.value, channel_type=2)
        header = {
            "Authorization": v_Authorization
        }
        return header


    def test_headers_get_admin(self):
        """
        管理端，platform_type = 2
        """
        user_id = base_data["init_user"]["admin_user_id"]
        v_Authorization = au.test_authorization_get(user_id, Platform.admin_platform.value)
        header = {
            "Authorization": v_Authorization
        }
        return header


headers = Headers()

if __name__ == '__main__':
    headers.test_headers_get_admin()

