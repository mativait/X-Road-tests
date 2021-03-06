# coding=utf-8

import unittest
from main.maincontroller import MainController
import st_management


"""
 UC SS_24: Log In to a Software Token
 RIA URL: https://jira.ria.ee/browse/XTKB-117
 Depends on finishing other test(s):
 Requires helper scenarios:
 X-Road version: 6.16.0
 """


class XroadLoginToken(unittest.TestCase):
    def test_xroad_login_token(self):
        main = MainController(self)

        # Set test name and number
        main.test_number = 'UC SS_24'
        main.log('TEST: UC SS_24: Log In to a Software Token')

        main.test_name = self.__class__.__name__

        ssh_host = main.config.get('ss2.ssh_host')
        ssh_username = main.config.get('ss2.ssh_user')
        ssh_password = main.config.get('ss2.ssh_pass')

        main.url = main.config.get('ss2.host')
        main.username = main.config.get('ss2.user')
        main.password = main.config.get('ss2.pass')
        token_pin = str(main.config.get('cp.token_pin'))

        '''Configure the service'''
        test_ss_backup_upload = st_management.test_edit_conf(case=main, ssh_host=ssh_host, ssh_username=ssh_username,
                                                             ssh_password=ssh_password, token_pin=token_pin)

        try:
            '''Open webdriver'''
            main.reload_webdriver(url=main.url, username=main.username, password=main.password)

            '''Run the test'''
            test_ss_backup_upload()
        except:
            main.log('Xroad_log_into_a_software_token: Failed to Log In to a Software Token')
            main.save_exception_data()
            assert False
        finally:
            '''Test teardown'''
            main.tearDown()
