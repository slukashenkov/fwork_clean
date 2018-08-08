import sys
import logging
import logging.config

#import yaml
import os
import json
import _json
#import jsonpickle
from subprocess import Popen

'''
    default_path='C:\\data_from\\kronshtadt\\QA\\BL\\AutomationFrameworkDesign\\bl_frame_work\\test_bl\\test_bl_configs\\logging_conf.json',
                 default_level=logging.INFO,
                 logging_dir='BL_LOGGING_DIR',
                 log_file='BL_LOG_CONF_FNAME',
                 log_file_dir='BL_LOG_CONF_PATH',
                 log_conf_full='BL_LOG_CONF_PATH_TOF',
                 cmd_path_commands='C:\\data_from\\kronshtadt\\QA\\BL\\AutomationFrameworkDesign\\bl_frame_work\\env_setup.cmd',
                 cmd_path='C:\\data_from\\kronshtadt\\QA\\BL\\AutomationFrameworkDesign\\bl_frame_work\\'
'''


class LoggingTools():
    def __init__(self,
                 default_path = None,
                 default_level = None,
                 logging_dir = None,
                 log_file = None,
                 log_file_dir = None,
                 log_conf_full = None
                 ):
            """
            Logger is not set yet
            """
            self.logger_is_set = False

            '''
            Get ready to setup everything.
            TO DO: read from structure is badly needed.             
            '''
            self.default_path = default_path
            self.default_level = default_level
            self.logging_dir = logging_dir
            self.log_file = log_file
            self.log_file_dir = log_file_dir
            self.log_conf_full = log_conf_full



            self.setup_logging(self.default_path,
                               self.default_level,
                               self.logging_dir,
                               self.log_file,
                               self.log_file_dir,
                               self.log_conf_full
                               )


    def setup_logging(self,
                    default_path,
                    default_level,
                    logging_dir,
                    log_file,
                    log_file_dir,
                    log_conf_full
                     ):
            '''
            Extract from .cmd file:

                ::Logging configuration
                SETx BL_LOG_CONF_PATH "d:\data_from\python\projects\bl_frame_work_25_05_18_02\bl_frame_work\test_bl\test_sonata_plugin\configs_sonata\logging_conf.json"
                SETx BL_LOG_CONF_PATH_TOF "d:\data_from\python\projects\bl_frame_work_25_05_18_02\bl_frame_work\test_bl\test_sonata_plugin\configs_sonata\logging_conf.json"
                SETx BL_LOG_CONF_FNAME "logging_conf.json"
                SETx BL_LOGGING_DIR "d:\data_from\python\projects\bl_frame_work_25_05_18_02\bl_frame_work"

                 logging_dir = 'BL_LOGGING_DIR',
                        log_file = 'BL_LOG_CONF_FNAME',
                        log_file_dir = 'BL_LOG_CONF_PATH',
                        log_conf_full ='BL_LOG_CONF_PATH_TOF',


            default_path='D:\\data_from\python\\projects\\bl_frame_work_25_05_18_02\\bl_frame_work\\test_bl\\test_bl_configs\\logging_conf.json',
            default_level=logging.INFO,
            env_key_log_dir='BL_CONF_PATH',
            log_file='BL_LOG_CONF_FILE',
            cmd_path_commands='D:\\data_from\\python\\projects\\bl_frame_work_25_05_18_02\\bl_frame_work\\env_setup.cmd',
            cmd_path = 'D:\\data_from\\python\\projects\\bl_frame_work_25_05_18_02\\bl_frame_work'
            '''

            """
            Run the cmd file to set env variables
    
            :param default_level:
            :param env_key:
            :return:
            """

            #p = Popen(cmd_path_commands, cwd=cmd_path)
            #stdout, stderr = p.communicate()

            """
            Setup logging configuration
            """
            #log_file="logging_conf.json"
            '''
            Just a reminder:
            Extract from .cmd file:
               
                ::Logging configuration
                SETx BL_LOG_CONF_PATH "d:\data\python\projects\bl_frame_work_25_05_18_02\bl_frame_work\test_bl\test_sonata_plugin\configs_sonata\logging_conf.json"
                SETx BL_LOG_CONF_PATH_TOF "d:\data\python\projects\bl_frame_work_25_05_18_02\bl_frame_work\test_bl\test_sonata_plugin\configs_sonata\logging_conf.json"
                SETx BL_LOG_CONF_FNAME "logging_conf.json"
                SETx BL_LOGGING_DIR "d:\data\python\projects\bl_frame_work_25_05_18_02\bl_frame_work"
                
                        logging_dir = 'BL_LOGGING_DIR',
                        log_file = 'BL_LOG_CONF_FNAME',
                        log_file_dir = 'BL_LOG_CONF_PATH',
                        log_conf_full ='BL_LOG_CONF_PATH_TOF'
            

            log_file_name = os.getenv(env_key_log_file, None)
            log_file_dir = os.getenv(env_key_log_file_dir, None)
            logging_conf_full_to_file=  os.getenv(log_conf_full, None)
            '''
            path_logs_conf_full = ''.join((str(log_file_dir),"\\",str(log_file)))


            path=default_path

            if path_logs_conf_full:
                path = path_logs_conf_full
                #path = ''.join((str(path_confs),"\\",str(log_file)))
            if os.path.exists(path):
                with open(path, 'rt') as f:
                    config = json.load(f)
                    logging.config.dictConfig(config)
            else:
                logging.basicConfig(level=default_level)


            self.logger_is_set=True


    def get_logger(self,
                   mod_name):
            curr_mod_logger=logging.getLogger(mod_name)
            return curr_mod_logger

if __name__ == "__main__":
            from subprocess import Popen, Popen, Popen, Popen

            lt=LoggingTools()
            #lt.setup_logging()
            logger=lt.get_logger(__name__)
            logger.info("got logger")