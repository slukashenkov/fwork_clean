import unittest, time, xmlrunner, datetime



if __name__ == '__main__':

        counter = 0
        date_now = datetime.datetime.now()
        date_now_str = date_now.strftime("%Y-%m-%d_%H-%M")
        loader = unittest.TestLoader()
        start_dir = 'C:\\data\\kronshtadt\\QA\\BL\\AutomationFrameworkDesign\\bl_frame_work\\test_bl'
        suite = loader.discover(start_dir)
        #runner = xmlrunner.XMLTestRunner(output='./sonata-xml-test-reports-'+str(counter)+' '+date_now_str)
        runner = xmlrunner.XMLTestRunner(output='C:/data/kronshtadt/QA/BL/Test_Logs/sonata-xml-test-reports-' + str(counter) + ' ' + date_now_str)

        '''
        while counter != 5:
                print("LOOP --------> " + str(counter))
                if counter !=0:
                        del loader
                        loader = unittest.TestLoader()
                        start_dir = 'C:\\data\\kronshtadt\\QA\\BL\\AutomationFrameworkDesign\\bl_frame_work\\test_bl'
                        del suite
                        suite = loader.discover(start_dir)
                        del runner
                        runner = xmlrunner.XMLTestRunner(output='./sonata-xml-test-reports-'+str(counter)+' '+date_now_str)

                result = runner.run(suite)
                counter = counter + 1
        '''

        result = runner.run(suite)