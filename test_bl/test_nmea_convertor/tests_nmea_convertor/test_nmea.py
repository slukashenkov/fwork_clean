import unittest, time, xmlrunner
from collections import deque


from test_bl.test_bl_tools import var_utils, external_scripts, udp_sender, udp_server, logging_tools
from test_bl.test_bl_tools.udp_server import UdpPayloadHandler

#import send_receive_sonata, sonata_nmea_msgs_content_process
#import sonata_send_recieve_properties, sonata_suite_config
#import var_utils, external_scripts


class NMEAConversionTests(unittest.TestCase):
        """Logging tools"""
        '''Logging'''

        lt = logging_tools.LoggingTools(default_level = "DEBUG" ,
                                        logging_dir = "C:\\data\\kronshtadt\\QA\\BL\\AutomationFrameworkDesign\\bl_frame_work",
                                        log_file = "logging_conf.json",
                                        log_file_dir = "C:\\data\\kronshtadt\\QA\\BL\\AutomationFrameworkDesign\\bl_frame_work",
                                        log_conf_full = "C:\data\kronshtadt\QA\BL\AutomationFrameworkDesign\bl_frame_work\test_bl\test_sonata_plugin\configs_sonata\logging_conf.json"
                                    )

        msg_q = deque()
        msg_l = []

        udp_sender = udp_sender.UdpSender(msg_iterator = msg_l.__iter__(),
                                            delay = 1,
                                            logging_tools = lt,
                                            ip_to = "10.11.10.12",
                                            port_to = "55555",
                                            msg_queue = msg_q,
                                            msg_sent_evnt = None,
                                            msg_src_slctr = 0
                                            )

        address = ('10.11.10.12', 55557)
        data_in = []
        udp_udp_server = udp_server.UdpServer(server_address    =address,
                                             handler_class      =UdpPayloadHandler,
                                             data_in            =data_in,
                                             curr_log_tools     = lt,
                                             conf_in            = None,
                                             msg_res_event      = None
                                            )
        @classmethod
        def tearDownClass(self):

            return

        def setUp(self):

            return

        def tearDown(self):

            return

        @unittest.skip("test_nmea01 is not needed now")
        def test_nmea01(self):

            return


if __name__ == '__main__':
        unittest.main()