# -*- coding: utf-8 -*-
import urllib2
from variables import strings, errors
from webframework import TESTDATA
from webframework.extension.base.setupTest import SetupTest
from webframework.extension.parsers.parameter_parser import get_all_parameters
from webframework.extension.util.common_utils import *
from time import sleep
from pagemodel.open_application import Open_application
from pagemodel.ss_login import Ss_login
from common_lib.common_lib import Common_lib
from common_lib.component_cs import Component_cs
from common_lib.component_common import Component_common
from common_lib.common_lib_ssh import Common_lib_ssh
from common_lib.component_cs_conf_mgm import Component_cs_conf_mgm
from common_lib.component_cs_sidebar import Component_cs_sidebar
from common_lib.component_cs_system_settings import Component_cs_system_settings
from pagemodel.cs_conf_mgm import Cs_conf_mgm
from pagemodel.cs_sidebar import Cs_sidebar
from pagemodel.cs_system_settings import Cs_system_settings

class Xroad_global_configuration(SetupTest):
    """
    .. _document: https://github.com/ria-ee/X-Road/blob/develop/doc/UseCases/uc-gconf_x-road_use_case_model_for_global_configuration_distribution_1.4_Y-883-8.md
    .. _GCONF 2.2.1: https://github.com/ria-ee/X-Road/blob/develop/doc/UseCases/uc-gconf_x-road_use_case_model_for_global_configuration_distribution_1.4_Y-883-8.md#221-uc-gconf_01-view-a-configuration-source
    .. _GCONF 2.2.2: https://github.com/ria-ee/X-Road/blob/develop/doc/UseCases/uc-gconf_x-road_use_case_model_for_global_configuration_distribution_1.4_Y-883-8.md#222-uc-gconf_02-download-a-configuration-source-anchor-file
    .. _GCONF 2.2.3: https://github.com/ria-ee/X-Road/blob/develop/doc/UseCases/uc-gconf_x-road_use_case_model_for_global_configuration_distribution_1.4_Y-883-8.md#223-uc-gconf_03-re-create-a-configuration-source-anchor
    .. _GCONF 2.2.4: https://github.com/ria-ee/X-Road/blob/develop/doc/UseCases/uc-gconf_x-road_use_case_model_for_global_configuration_distribution_1.4_Y-883-8.md#224-uc-gconf_04-describe-optional-configuration-part-data
    .. _GCONF 2.2.5: https://github.com/ria-ee/X-Road/blob/develop/doc/UseCases/uc-gconf_x-road_use_case_model_for_global_configuration_distribution_1.4_Y-883-8.md#225-uc-gconf_05-upload-an-optional-configuration-part-file
    .. _GCONF 2.2.6: https://github.com/ria-ee/X-Road/blob/develop/doc/UseCases/uc-gconf_x-road_use_case_model_for_global_configuration_distribution_1.4_Y-883-8.md#226-uc-gconf_06-download-a-configuration-part-file
    .. _GCONF 2.2.7: https://github.com/ria-ee/X-Road/blob/develop/doc/UseCases/uc-gconf_x-road_use_case_model_for_global_configuration_distribution_1.4_Y-883-8.md#227-uc-gconf_07-log-in-to-a-software-security-token
    .. _GCONF 2.2.9: https://github.com/ria-ee/X-Road/blob/develop/doc/UseCases/uc-gconf_x-road_use_case_model_for_global_configuration_distribution_1.4_Y-883-8.md#229-uc-gconf_09-log-out-of-a-software-security-token
    .. _GCONF 2.2.11: https://github.com/ria-ee/X-Road/blob/develop/doc/UseCases/uc-gconf_x-road_use_case_model_for_global_configuration_distribution_1.4_Y-883-8.md#2211-uc-gconf_11-add-a-configuration-source-signing-key
    .. _GCONF 2.2.12: https://github.com/ria-ee/X-Road/blob/develop/doc/UseCases/uc-gconf_x-road_use_case_model_for_global_configuration_distribution_1.4_Y-883-8.md#2212-uc-gconf_12-activate-a-configuration-source-signing-key
    .. _GCONF 2.2.13: https://github.com/ria-ee/X-Road/blob/develop/doc/UseCases/uc-gconf_x-road_use_case_model_for_global_configuration_distribution_1.4_Y-883-8.md#2213-uc-gconf_13-delete-a-configuration-source-signing-key
    .. _GCONF 2.2.14: https://github.com/ria-ee/X-Road/blob/develop/doc/UseCases/uc-gconf_x-road_use_case_model_for_global_configuration_distribution_1.4_Y-883-8.md#2214-uc-gconf_14-view-system-parameters
    .. _GCONF 2.2.15: https://github.com/ria-ee/X-Road/blob/develop/doc/UseCases/uc-gconf_x-road_use_case_model_for_global_configuration_distribution_1.4_Y-883-8.md#2215-uc-gconf_15-edit-the-address-of-the-central-server
    .. _GCONF 2.2.16: https://github.com/ria-ee/X-Road/blob/develop/doc/UseCases/uc-gconf_x-road_use_case_model_for_global_configuration_distribution_1.4_Y-883-8.md#2216-uc-gconf_16-parse-user-input
    .. _GCONF 2.2.17: https://github.com/ria-ee/X-Road/blob/develop/doc/UseCases/uc-gconf_x-road_use_case_model_for_global_configuration_distribution_1.4_Y-883-8.md#2217-uc-gconf_17-generate-a-configuration-anchor
    .. _GCONF 2.2.18: https://github.com/ria-ee/X-Road/blob/develop/doc/UseCases/uc-gconf_x-road_use_case_model_for_global_configuration_distribution_1.4_Y-883-8.md#2218-uc-gconf_18-generate-configuration
    .. _GCONF 2.2.19: https://github.com/ria-ee/X-Road/blob/develop/doc/UseCases/uc-gconf_x-road_use_case_model_for_global_configuration_distribution_1.4_Y-883-8.md#2219-uc-gconf_19-handle-a-configuration-download-request

    Xroad cases for global configurations

    Use cases `document`_

    **Use cases:**
        * `Global configuration view source`_
            * `GCONF 2.2.1`_: View a Configuration Source
        * `Global configuration download and recreate`_
            * `GCONF 2.2.2`_: Download a Configuration Source Anchor File
            * `GCONF 2.2.3`_: Re-Create a Configuration Source Anchor
                * Extension 2a. The process of generating the anchor terminated with an error message. (postpone?)
        * `Optional conf parts`_
            * `GCONF 2.2.4`_: Describe Optional Configuration Part Data
            * `GCONF 2.2.5`_: Upload an Optional Configuration Part File
                * Extension 3a. A validator is not described for this configuration part.
                * Extension 3b. The system is unable to find the described validation program.
                * Extension 4a. The validation succeeded with validation errors.
            * `GCONF 2.2.6`_: Download a Configuration Part File
        * `Login and log out software security token`_
            * `GCONF 2.2.7`_: Log In to a Software Security Token
                * Extension 3a: The parsing of the user input terminated with an error message.
                * Extension 4a: The entered PIN code is incorrect.
            * `GCONF 2.2.9`_: Log Out of a Software Security Token
        * `Activate and delete config signing key`_
            * `GCONF 2.2.11`_: Add a Configuration Source Signing Key
                * Extension 4a. Key generation fails because the token is not logged in to
            * `GCONF 2.2.12`_: Activate a Configuration Source Signing Key
                * Extension 3a: CS administrator cancels the key activation
            * `GCONF 2.2.13`_: Delete a Configuration Source Signing Key
                * Extension 3a: CS administrator cancels the key deletion
                * Extension 7a: System fails to delete the signing key form the security token.
        * `View sys param and edit address of cs`_
            * `GCONF 2.2.14`_: View System Parameters
            * `GCONF 2.2.15`_: Edit the Address of the Central Server
                * Extension 3a: The parsing of the user input terminated with an error message
                * Extension 4a: The inserted address is not valid
            * `GCONF 2.2.16`_: Parse User Input (bug)
                * Extension 2a. One or more mandatory fields are not filled.
                * Extension 3a. The user input exceeds 255 symbols.
        * `Generate configuration`_
            * `GCONF 2.2.18`_: Generate Configuration
                * Extension 1c. The generation of the configuration part files failed for any other reason than the ones stated in extensions 1a and 1b.
        * `Handle configuration download request`_
            * `GCONF 2.2.19`_: Handle a Configuration Download Request
        * Postponed
            * `GCONF 2.2.17`_: Generate a Configuration Anchor (postpone)
                * Extension 1a. System did not find any configuration signing keys for the configuration source. (postpone)
            * `GCONF 2.2.18`_: Generate Configuration
                * Extension 1a. The generation of the configuration part files failed because the central server address is not configured. (postpone)
                * Extension 1b. The generation of the configuration part files failed because the management service provider is not configured. (postpone)
            * `GCONF 2.2.19`_: Handle a Configuration Download Request
                * Extension 2a: Request cannot be served. (postpone)

    **Changelog:**
        * 2.1.2017
            * `2.2.4`_, `2.2.5`_, `2.2.6`_, `2.2.7`_, `2.2.11`_, `2.2.13`_ Test cases done
        * 20.09.2017
            * Links added to md use case documentation
        * 11.07.2017
            * Documentation updated
    """
    common_utils = CommonUtils()
    open_application = Open_application()
    ss_login = Ss_login()
    common_lib = Common_lib()
    component_cs = Component_cs()
    component_common = Component_common()
    common_lib_ssh = Common_lib_ssh()
    component_cs_conf_mgm = Component_cs_conf_mgm()
    component_cs_sidebar = Component_cs_sidebar()
    component_cs_system_settings = Component_cs_system_settings()
    cs_conf_mgm = Cs_conf_mgm()
    cs_sidebar = Cs_sidebar()
    INI_FILE = "foo.ini"
    cs_system_settings = Cs_system_settings()

    @classmethod
    def setUpTestSet(self):
        """
        Method that runs before every unittest

        **Test steps:**
                * **Step 1:** :func:`~pagemodel.autogen_browser = self.Autogen_browser = self.common_utils`
        """
        self.autogen_browser = self.common_utils.open_browser()

    @classmethod
    def tearDownTestSet(self):
        """
        Method that runs after every unittest

        **Test steps:**
                * **Step 1:** :func:`~webframework.extension.util.common_utils.CommonUtils.close_all_browsers`
        """
        self.common_utils.close_all_browsers()

    def setUp(self):
        """
        Method that runs before every test case

        **Test steps:**
            * **Step 1: set to default before test case**
                * :func:`~common_lib.common_lib.Common_lib.delete_files_with_extension`, *TESTDATA[u'paths'][u'downloads_folder']*, *u'.xml'*
                * :func:`~pagemodel.start_log_time = self.Start_log_time = self.common_lib`
                * :func:`~common_lib.common_lib_ssh.Common_lib_ssh.empty_all_logs_from_server`, *"ss1_url"*
                * :func:`~common_lib.common_lib_ssh.Common_lib_ssh.empty_all_logs_from_server`, *"cs_url"*
        """
        self.login_to_token = False
        # Step Set to default before test case
        self.common_lib.delete_files_with_extension(TESTDATA[u'paths'][u'downloads_folder'], u'.xml')
        self.start_log_time = self.common_lib.get_log_utc_time()
        self.common_lib_ssh.empty_all_logs_from_server("ss1_url")
        self.common_lib_ssh.empty_all_logs_from_server("cs_url")

    def tearDown(self):
        """
        Method that runs after every test case

        **Test steps:**
            * **Step 1: log out if logged in**
                * :func:`~common_lib.common_lib.Common_lib.log_out`
            * **Step 2: revert to defaults**
                * :func:`~common_lib.common_lib.Common_lib.delete_files_with_extension`, *TESTDATA[u'paths'][u'downloads_folder']*, *u'.xml'*
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.delete_conf_part_file`, *self.INI_FILE*
                * :func:`~common_lib.common_lib_ssh.Common_lib_ssh.get_all_logs_from_server`, *u'ss1_url'*
                * :func:`~common_lib.common_lib_ssh.Common_lib_ssh.find_exception_from_logs_and_save`
                * :func:`~common_lib.common_lib_ssh.Common_lib_ssh.get_all_logs_from_server`, *u'cs_url'*
                * :func:`~common_lib.common_lib_ssh.Common_lib_ssh.find_exception_from_logs_and_save`
        """
        if self.login_to_token:
            if self.ss_login.verify_is_login_page():
                self.component_cs.login(section=u'cs_url')
            self.component_cs_sidebar.open_global_configuration_view()
            self.component_cs_conf_mgm.log_in_to_software_token(section=u'cs_url')

        self.open_application.open_application_url(TESTDATA[u'cs_url'])
        # Step log out if logged in
        if not self.ss_login.verify_is_login_page():
            self.common_lib.log_out()

        # Step revert to defaults
        self.common_lib.delete_files_with_extension(TESTDATA[u'paths'][u'downloads_folder'], u'.xml')
        try:
            # Delete generated conf part file
            self.component_cs_conf_mgm.delete_conf_part_file(self.INI_FILE)
        except:
            pass

        stop_log_time = self.common_lib.get_log_utc_time()
        if not self.is_last_test_passed():
            _, copy_log = self.get_log_file_paths()
            self.common_lib_ssh.get_all_logs_from_server(u'ss1_url')
            self.common_lib_ssh.find_exception_from_logs_and_save(self.start_log_time,
                                                                  stop_log_time,
                                                                  u'ss1_url',
                                                                  copy_log)
            self.common_lib_ssh.get_all_logs_from_server(u'cs_url')
            self.common_lib_ssh.find_exception_from_logs_and_save(self.start_log_time,
                                                                  stop_log_time,
                                                                  u'cs_url',
                                                                  copy_log)

    def test_global_configuration_view_source(self):
        """
        Test case for viewing global configuration view source

        **Use cases:**
            * `GCONF 2.2.1`_: View a Configuration Source

        **Test steps:**
            * **Step 1: login to central server and open configuration view**
                * :func:`~common_lib.component_cs.Component_cs.login`, *section=u'cs_url'*
                * :func:`~common_lib.component_cs_sidebar.Component_cs_sidebar.open_global_configuration_view`
            * **Step 2: verify displayed information internalconf**
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.verify_internal_configuration_view`
            * **Step 3: verify displayed information externalconf**
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.verify_external_configuration_view`
            * **Step 4: log out**
                * :func:`~common_lib.common_lib.Common_lib.log_out`
        """
        # Step Login to central server and open configuration view
        self.component_cs.login(section=u'cs_url')
        self.component_cs_sidebar.open_global_configuration_view()

        # Step Verify displayed information internalconf
        self.component_cs_conf_mgm.verify_internal_configuration_view()

        # Step Verify displayed information externalconf
        self.component_cs_conf_mgm.verify_external_configuration_view()

        # Step Log out
        self.common_lib.log_out()

    def test_global_configuration_download_and_recreate(self):
        """
        Test case for downloading source anchor and recreating it

        **Use cases:**
            * `GCONF 2.2.2`_: Download a Configuration Source Anchor File
            * `GCONF 2.2.3`_: Re-Create a Configuration Source Anchor
                * Extension 2a. The process of generating the anchor terminated with an error message. (postpone?)

        **Test steps:**
            * **Step 1: login to central server and open configuration view**
                * :func:`~common_lib.component_cs.Component_cs.login`, *section=u'cs_url'*
                * :func:`~common_lib.component_cs_sidebar.Component_cs_sidebar.open_global_configuration_view`
            * **Step 2: download configuration source anchor**
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.download_source_anchor_from_cs`
            * **Step 3: recreate configuration source anchor**
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.recreate_source_anchor_from_cs`
            * **Step 4: log out**
                * :func:`~common_lib.common_lib.Common_lib.log_out`
        """
        # Step Login to central server and open configuration view
        self.component_cs.login(section=u'cs_url')
        self.component_cs_sidebar.open_global_configuration_view()

        # Step Download configuration source anchor
        self.component_cs_conf_mgm.download_source_anchor_from_cs()

        # Step Recreate configuration source anchor
        self.component_cs_conf_mgm.recreate_source_anchor_from_cs()

        # Step Log out
        self.common_lib.log_out()

    def test_optional_conf_parts(self):
        """
        Test all optional configuration part cases

        **Use cases:**
            * `GCONF 2.2.4`_: Describe Optional Configuration Part Data
            * `GCONF 2.2.5`_: Upload an Optional Configuration Part File
                * Extension 3a. A validator is not described for this configuration part.
                * Extension 3b. The system is unable to find the described validation program.
                * Extension 4a. The validation succeeded with validation errors.
            * `GCONF 2.2.6`_: Download a Configuration Part File

        **Test steps:**
            * **Step 1: login to central server and open configuration view**
                * :func:`~common_lib.component_cs.Component_cs.login`, *section=u'cs_url'*
                * :func:`~common_lib.component_cs_sidebar.Component_cs_sidebar.open_global_configuration_view`
            * **Step 2: generate optional configuration part file with validation file**
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.generate_conf_part_file`, *self.INI_FILE*, *identifier*, *file_name*, *existing_val_script*
            * **Step 3: upload configuration part file**
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.upload_configuration_part_file`, *identifier*, *valid_part_file*
            * **Step 4: download configuration part file**
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.download_configuration_part_file`, *identifier*
            * **Step 5: upload configuration part file fail**
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.upload_conf_part_validation_fail`, *identifier*, *invalid_part_file*
            * **Step 6: generate optional configuration part file with out validation file**
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.generate_conf_part_file`, *self.INI_FILE*, *identifier*, *file_name*
            * **Step 7: upload configuration part file**
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.upload_configuration_part_file`, *identifier*, *valid_part_file*
            * **Step 8: generate optional configuration part file with missing validation file**
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.generate_conf_part_file`, *self.INI_FILE*, *identifier*, *file_name*, *missing_val_script*
            * **Step 9: upload configuration part file fail missing validation**
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.upload_conf_part_validation_fail_missing_validation`
            * **Step 10: delete generated conf part file**
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.delete_conf_part_file`, *self.INI_FILE*
            * **Step 11: log out**
                * :func:`~common_lib.common_lib.Common_lib.log_out`
        """
        # Configuration part upload files
        valid_part_file = os.path.join(os.getcwd(), "data", "valid_conf_part.xml")
        invalid_part_file = os.path.join(os.getcwd(), "data", "invalid_conf_part.xml")

        # Generated conf part file
        identifier = u'FOO'
        file_name = u'foo.xml'
        existing_val_script = u'/usr/share/xroad/scripts/validate-monitoring-params.sh'
        missing_val_script = u'/usr/share/xroad/scripts/validate.sh'

        # Step Login to central server and open configuration view
        self.component_cs.login(section=u'cs_url')
        self.component_cs_sidebar.open_global_configuration_view()

        # Step Generate optional configuration part file with validation file
        self.component_cs_conf_mgm.generate_conf_part_file(self.INI_FILE, identifier, file_name, existing_val_script)
        # Step Upload configuration part file
        self.component_cs_conf_mgm.upload_configuration_part_file(identifier, valid_part_file)
        # Step Download configuration part file
        self.component_cs_conf_mgm.download_configuration_part_file(identifier)

        # Step Upload configuration part file fail
        self.component_cs_conf_mgm.upload_conf_part_validation_fail(identifier, invalid_part_file)

        # Step Generate optional configuration part file with out validation file
        self.component_cs_conf_mgm.generate_conf_part_file(self.INI_FILE, identifier, file_name)
        # Step Upload configuration part file
        self.component_cs_conf_mgm.upload_configuration_part_file(identifier, valid_part_file)

        # Step Generate optional configuration part file with missing validation file
        self.component_cs_conf_mgm.generate_conf_part_file(self.INI_FILE, identifier, file_name, missing_val_script)
        # Step Upload configuration part file fail missing validation
        self.component_cs_conf_mgm.upload_conf_part_validation_fail_missing_validation(identifier, valid_part_file,
                                                                                       missing_val_script)

        # Step Delete generated conf part file
        self.component_cs_conf_mgm.delete_conf_part_file(self.INI_FILE)

        # Step Log out
        self.common_lib.log_out()

    def test_login_and_log_out_software_security_token(self):
        """
        Test case for logging in and logging out software security token

        **Use cases:**
            * `GCONF 2.2.7`_: Log In to a Software Security Token
                * Extension 3a: The parsing of the user input terminated with an error message.
                * Extension 4a: The entered PIN code is incorrect.
            * `GCONF 2.2.9`_: Log Out of a Software Security Token

        **Test steps:**
            * **Step 1: login to central server and open configuration view**
                * :func:`~common_lib.component_cs.Component_cs.login`, *section=u'cs_url'*
                * :func:`~common_lib.component_cs_sidebar.Component_cs_sidebar.open_global_configuration_view`
            * **Step 2: log out software token**
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.logout_software_token`
            * **Step 3: log in software token empty pin**
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.log_in_to_software_token_empty_pin`, *section=u'empty_pin'*
            * **Step 4: log in software token invalid pin**
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.log_in_to_software_token_invalid_pin`, *section=u'invalid_cs_url'*
            * **Step 5: log in software token**
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.log_in_to_software_token`, *section=u'cs_url'*
            * **Step 6: log out**
                * :func:`~common_lib.common_lib.Common_lib.log_out`
        """
        # Step Login to central server and open configuration view
        self.component_cs.login(section=u'cs_url')
        self.component_cs_sidebar.open_global_configuration_view()

        # Step Log out software token
        self.component_cs_conf_mgm.logout_software_token()
        self.login_to_token = True

        # Step Log in software token empty pin
        self.component_cs_conf_mgm.log_in_to_software_token_empty_pin(section=u'empty_pin')

        # Step Log in software token invalid pin
        self.component_cs_conf_mgm.log_in_to_software_token_invalid_pin(section=u'invalid_cs_url')

        # Step Log in software token
        self.component_cs_conf_mgm.log_in_to_software_token(section=u'cs_url')
        self.login_to_token = False

        # Step Log out
        self.common_lib.log_out()

    def test_activate_and_delete_config_signing_key(self):
        """
        Test case for activating and deleting config signing key

        **Use cases:**
            * `GCONF 2.2.11`_: Add a Configuration Source Signing Key
                * Extension 4a. Key generation fails because the token is not logged in to
            * `GCONF 2.2.12`_: Activate a Configuration Source Signing Key
                * Extension 3a: CS administrator cancels the key activation
            * `GCONF 2.2.13`_: Delete a Configuration Source Signing Key
                * Extension 3a: CS administrator cancels the key deletion
                * Extension 7a: System fails to delete the signing key form the security token.

        **Test steps:**
            * **Step 1: login to central server and open configuration view**
                * :func:`~common_lib.component_cs.Component_cs.login`, *section=u'cs_url'*
                * :func:`~common_lib.component_cs_sidebar.Component_cs_sidebar.open_global_configuration_view`
            * **Step 2: generate signing key**
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.generate_config_key`
            * **Step 3: activate signing_key**
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.activate_newest_signing_key`
            * **Step 4: activate old signing key**
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.activate_oldest_signing_key`
            * **Step 5: delete signing key**
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.delete_newest_signing_key`
            * **Step 6: generate signing key**
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.generate_config_key`
            * **Step 7: get newest signing key**
            * **Step 8: delete signing key from console**
                * :func:`~common_lib.common_lib_ssh.Common_lib_ssh.delete_signing_key_from_signer_console`, *section=u'cs_url'*, *key=key*
            * **Step 9: delete signing key**
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.delete_signing_key_fail`, *key=key*
            * **Step 10: log out and generate key with out log in**
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.logout_software_token`
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.generate_config_key_not_logged_in`, *u'cs_url'*
            * **Step 11: delete signing key**
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.delete_newest_signing_key`
            * **Step 12: log out**
                * :func:`~common_lib.common_lib.Common_lib.log_out`
        """
        # Step Login to central server and open configuration view
        self.component_cs.login(section=u'cs_url')
        self.component_cs_sidebar.open_global_configuration_view()

        # Step Generate signing key
        self.component_cs_conf_mgm.generate_config_key()

        # Step Activate signing_key
        self.component_cs_conf_mgm.activate_newest_signing_key()

        # Step Activate old signing key
        self.component_cs_conf_mgm.activate_oldest_signing_key()

        # Step Delete signing key
        self.component_cs_conf_mgm.delete_newest_signing_key()

        # Step Generate signing key
        self.component_cs_conf_mgm.generate_config_key()
        # Step Get newest signing key
        key = self.cs_conf_mgm.get_newest_key_id()
        # Step Delete signing key from console
        self.common_lib_ssh.delete_signing_key_from_signer_console(section=u'cs_url', key=key)
        # Step Delete signing key
        self.component_cs_conf_mgm.delete_signing_key_fail(key=key)

        # Step log out and generate key with out log in
        self.component_cs_conf_mgm.logout_software_token()
        self.login_to_token = True
        self.component_cs_conf_mgm.generate_config_key_not_logged_in(u'cs_url')
        self.login_to_token = False
        # Step Delete signing key
        self.component_cs_conf_mgm.delete_newest_signing_key()

        # Step Log out
        self.common_lib.log_out()

    def test_view_sys_param_and_edit_address_of_cs(self):
        """
        Test case for viewing system parameters and editing address of central server

        **Use cases:**
            * `GCONF 2.2.14`_: View System Parameters
            * `GCONF 2.2.15`_: Edit the Address of the Central Server
                * Extension 3a: The parsing of the user input terminated with an error message
                * Extension 4a: The inserted address is not valid
            * `GCONF 2.2.16`_: Parse User Input (bug)
                * Extension 2a. One or more mandatory fields are not filled.
                * Extension 3a. The user input exceeds 255 symbols.

        **Test steps:**
            * **Step 1: login to central server and open system settings**
                * :func:`~common_lib.component_cs.Component_cs.login`, *section=u'cs_url'*
                * :func:`~common_lib.component_cs_sidebar.Component_cs_sidebar.open_system_settings_view`
            * **Step 2: change central server url**
                * :func:`~common_lib.component_cs_system_settings.Component_cs_system_settings.change_server_address`, *u'new_cs_url'*
            * **Step 3: verify edit cs address**
                * :func:`~common_lib.common_lib_ssh.Common_lib_ssh.verify_audit_log`, *section=u'cs_url'*, *event=strings.edit_cs_address*
            * **Step 4: change central server url invalid**
                * :func:`~common_lib.component_cs_system_settings.Component_cs_system_settings.change_server_address`, *u'invalid_cs_url'*
            * **Step 5: verify edit cs address failed**
                * :func:`~common_lib.common_lib_ssh.Common_lib_ssh.verify_audit_log`, *section=u'cs_url'*, *event=strings.edit_cs_address_failed*
            * **Step 6: verify address must be dns**
                * :func:`~common_lib.component_common.Component_common.verify_notice_message`, *message=strings.change_address_error*
                * :func:`~common_lib.component_cs_system_settings.Component_cs_system_settings.cancel_server_address_dlg`
            * **Step 7: change central server url invalid**
                * :func:`~common_lib.component_cs_system_settings.Component_cs_system_settings.change_server_address`, *section=u'invalid_cs_url'*
            * **Step 8: verify edit cs address failed**
                * :func:`~common_lib.common_lib_ssh.Common_lib_ssh.verify_audit_log`, *section=u'cs_url'*, *event=strings.edit_cs_address_failed*
            * **Step 9: verify address must be dns**
                * :func:`~common_lib.component_common.Component_common.verify_notice_message`, *message=strings.change_address_error*
            * **Step 10: input valid adress**
                * :func:`~common_lib.component_cs_system_settings.Component_cs_system_settings.input_server_address_in_dlg`, *section=u'cs_url'*
                * :func:`~common_lib.component_cs_system_settings.Component_cs_system_settings.confirm_server_address_dlg`
            * **Step 11: verify edit cs address**
                * :func:`~common_lib.common_lib_ssh.Common_lib_ssh.verify_audit_log`, *section=u'cs_url'*, *event=strings.edit_cs_address*
            * **Step 12: verify whitespace is parsed (disabled because of bug)**
            * **Step 13: verify parse input empty**
                * :func:`~common_lib.component_cs_system_settings.Component_cs_system_settings.change_server_address`, *section=u'empty_address'*
            * **Step 14: verify address must be dns**
                * :func:`~common_lib.component_common.Component_common.verify_notice_message`, *message=strings.parameter_missing.format(u'centralServerAddress'*
                * :func:`~common_lib.component_cs_system_settings.Component_cs_system_settings.cancel_server_address_dlg`
            * **Step 15: verify parse input max 255 characters**
                * :func:`~common_lib.component_cs_system_settings.Component_cs_system_settings.change_server_address`, *section=u'long_address'*
            * **Step 16: verify address must be dns**
                * :func:`~common_lib.component_common.Component_common.verify_notice_message`, *message=strings.parameter_exceed_255.format(u'centralServerAddress'*
                * :func:`~common_lib.component_cs_system_settings.Component_cs_system_settings.cancel_server_address_dlg`
            * **Step 17: log out**
                * :func:`~common_lib.common_lib.Common_lib.log_out`
        """
        # Step Login to central server and open system settings
        self.component_cs.login(section=u'cs_url')
        self.component_cs_sidebar.open_system_settings_view()

        # Step Change central server url
        self.component_cs_system_settings.change_server_address(u'new_cs_url')
        # Step Verify edit cs address
        self.common_lib_ssh.verify_audit_log(section=u'cs_url', event=strings.edit_cs_address)

        # Step Change central server url invalid
        self.component_cs_system_settings.change_server_address(u'invalid_cs_url')
        # Step Verify edit cs address failed
        self.common_lib_ssh.verify_audit_log(section=u'cs_url', event=strings.edit_cs_address_failed)
        # Step Verify address must be dns
        self.component_common.verify_notice_message(message=strings.change_address_error)
        self.component_cs_system_settings.cancel_server_address_dlg()

        # Step Change central server url invalid
        self.component_cs_system_settings.change_server_address(section=u'invalid_cs_url')
        # Step Verify edit cs address failed
        self.common_lib_ssh.verify_audit_log(section=u'cs_url', event=strings.edit_cs_address_failed)
        # Step Verify address must be dns
        self.component_common.verify_notice_message(message=strings.change_address_error)
        # Step Input valid adress
        self.component_cs_system_settings.input_server_address_in_dlg(section=u'cs_url')
        self.component_cs_system_settings.confirm_server_address_dlg()
        # Step Verify edit cs address
        self.common_lib_ssh.verify_audit_log(section=u'cs_url', event=strings.edit_cs_address)

        # Step Verify whitespace is parsed (disabled because of bug)
        #TESTDATA.create_section(section_name=u'whitespace_address')
        #TESTDATA[u'whitespace_address'][u'server_address'] = " " + TESTDATA[u'cs_url'][u'server_address']
        #self.component_cs_system_settings.change_server_address(section=u'whitespace_address')
        #self.cs_system_settings.verify_central_address_does_not_contain_whitespace()

        # Step Verify parse input empty
        TESTDATA.create_section(section_name=u'empty_address')
        TESTDATA[u'empty_address'][u'server_address'] = u''
        self.component_cs_system_settings.change_server_address(section=u'empty_address')
        # Step Verify address must be dns
        self.component_common.verify_notice_message(message=strings.parameter_missing.format(u'centralServerAddress'))
        self.component_cs_system_settings.cancel_server_address_dlg()

        # Step Verify parse input max 255 characters
        TESTDATA.create_section(section_name=u'long_address')
        TESTDATA[u'long_address'][u'server_address'] = u'x' * 256
        self.component_cs_system_settings.change_server_address(section=u'long_address')
        # Step Verify address must be dns
        self.component_common.verify_notice_message(message=strings.parameter_exceed_255.format(u'centralServerAddress'))
        self.component_cs_system_settings.cancel_server_address_dlg()

        # Step Log out
        self.common_lib.log_out()

    def test_generate_configuration(self):
        """
        Tests configuration generation that is automaticaly launched

        **Use cases:**
            * `GCONF 2.2.18`_: Generate Configuration
                * Extension 1c. The generation of the configuration part files failed for any other reason than the ones stated in extensions 1a and 1b.

        **Test steps:**
            * **Step 1: verify if v2 folder exists in server**
                * :func:`~common_lib.common_lib_ssh.Common_lib_ssh.verify_if_server_contains_directory`, *u'cs_url'*, *v2_path*
            * **Step 2: verify external and internal conf files from server**
                * :func:`~common_lib.common_lib_ssh.Common_lib_ssh.verify_if_server_contains_file`, *u'cs_url'*, *internal_conf_path*
                * :func:`~common_lib.common_lib_ssh.Common_lib_ssh.verify_if_server_contains_file`, *u'cs_url'*, *external_conf_path*
            * **Step 3: verify configuration directory time**
                * :func:`~pagemodel.fail(errors.Fail(errors.newest_configuration_file_too_old)`, *errors.newest_configuration_file_too_old*
            * **Step 4: verify newest configuration directory content**
                * :func:`~common_lib.common_lib_ssh.Common_lib_ssh.verify_if_server_contains_file`, *u'cs_url'*, *private_xml_file*
                * :func:`~common_lib.common_lib_ssh.Common_lib_ssh.verify_if_server_contains_file`, *u'cs_url'*, *shared_xml_file*
            * **Step 5: login to central server and open configuration view**
                * :func:`~common_lib.component_cs.Component_cs.login`, *section=u'cs_url'*
                * :func:`~common_lib.component_cs_sidebar.Component_cs_sidebar.open_global_configuration_view`
            * **Step 6: log out software token**
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.logout_software_token`
            * **Step 7: verify global configuration failing**
                * :func:`~webframework.extension.util.common_utils.CommonUtils.reload_page`
                * :func:`~common_lib.component_common.Component_common.verify_alert_message`, *strings.configuration_generation_fail*
                * :func:`~common_lib.common_lib_ssh.Common_lib_ssh.verify_jetty_log`, *u'cs_url'*, *strings.failed_to_generate_global_config*
            * **Step 8: log in software token**
                * :func:`~common_lib.component_cs_conf_mgm.Component_cs_conf_mgm.log_in_to_software_token`, *section=u'cs_url'*
            * **Step 9: log out**
                * :func:`~common_lib.common_lib.Common_lib.log_out`
        """
        v2_path = os.path.join(strings.generated_confs_directory, "V2")
        internal_conf_path = os.path.join(v2_path, "internalconf")
        external_conf_path = os.path.join(v2_path, "externalconf")

        # Step Verify if V2 folder exists in server
        self.common_lib_ssh.verify_if_server_contains_directory(u'cs_url', v2_path)

        # Step Verify external and internal conf files from server
        self.common_lib_ssh.verify_if_server_contains_file(u'cs_url', internal_conf_path)
        self.common_lib_ssh.verify_if_server_contains_file(u'cs_url', external_conf_path)

        # Step Verify configuration directory time
        v2_newest_dir = self.common_lib_ssh.get_newest_directory(u'cs_url', v2_path)
        server_time = self.common_lib_ssh.get_time(u'cs_url')
        time_length = len(self.common_lib_ssh.get_time(u'cs_url'))

        v2_newest_dir_time = int(v2_newest_dir[:time_length-1])
        server_time = int(server_time)
        time_since_last_generation = (server_time - v2_newest_dir_time)
        configuration_timeout = int(TESTDATA.get_parameter(u'cs_url', u'configuration_timeout'))

        print("time since last dir generation", time_since_last_generation)
        if time_since_last_generation >= configuration_timeout:
            self.fail(errors.newest_configuration_file_too_old)

        # Step Verify newest configuration directory content
        newest_directory_path = os.path.join(v2_path, v2_newest_dir)
        private_xml_file = os.path.join(newest_directory_path, u'private-params.xml')
        shared_xml_file = os.path.join(newest_directory_path, u'shared-params.xml')

        self.common_lib_ssh.verify_if_server_contains_file(u'cs_url', private_xml_file)
        self.common_lib_ssh.verify_if_server_contains_file(u'cs_url', shared_xml_file)

        # Step Login to central server and open configuration view
        self.component_cs.login(section=u'cs_url')
        self.component_cs_sidebar.open_global_configuration_view()

        # Step Log out software token
        self.component_cs_conf_mgm.logout_software_token()
        self.login_to_token = True

        # Step Verify global configuration failing
        sleep(configuration_timeout)
        self.common_utils.reload_page()
        self.component_common.verify_alert_message(strings.configuration_generation_fail)
        self.common_lib_ssh.verify_jetty_log(u'cs_url', strings.failed_to_generate_global_config)

        # Step Log in software token
        self.component_cs_conf_mgm.log_in_to_software_token(section=u'cs_url')
        self.login_to_token = False

        # Step Log out
        self.common_lib.log_out()

    def test_handle_configuration_download_request(self):
        """
        Tests if central server configuration downloads work

        **Use cases:**
            * `GCONF 2.2.19`_: Handle a Configuration Download Request

        **Test steps:**
            * **Step 1: test internalconf url download**
                * :func:`~webframework.extension.util.common_utils.CommonUtils.fail`, *"Internal conf not found"*
        """
        # Step Test internalconf url download
        internal_conf_url = TESTDATA.get_parameter(section_name=u'cs_url', parameter_name=u'internal_conf_url')
        print ("testing", internal_conf_url)
        content = self.common_lib_ssh.curl_url(u'cs_url',internal_conf_url)
        if "404 Not Found" in content:
            self.common_utils.fail("Internal conf not found")
        print content
