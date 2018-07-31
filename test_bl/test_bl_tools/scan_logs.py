import re, sys

class ScanLogs():
    def __init__(self,
                 conf_in = None,
                 logs_location = None
                 ):

        self.conf = conf_in

        if conf_in != None:
            self.logs_location = conf_in.logs.location
        if logs_location!=None:
            self.logs_location = self.conf.logs_location
        return

    def scan_logs(self,
                  pattern_in=None
                  ):
        """"""

        '''SET THE PATTERN'''
        if pattern_in ==None:
            pattern=self.conf.test_pattern
        else:
            pattern = pattern_in

        '''GET THE BLOODY LOG first '''
        log_for_parsing = self.log_reader(self.logs_location)

        matches = []
        for line in log_for_parsing:
            res = self.parse_line(line_in=line,
                                  pattern_in=pattern)
            if res != None:
                matches.append(res)
        return matches

    def parse_line(self,
                   line_in = None,
                   pattern_in = None):
        srch = re.compile(pattern_in)
        res=srch.search(line_in)
        return res

    def log_reader(self,
                    logfile = None
                   ):
        if logfile == None:
            raise Exception("NO PATH to the File To parse")
        try:
            log = open(logfile, 'r')
        except IOError:
            print("You must specify a valid file to parse")
            print(__doc__)
            sys.exit(1)
        return log

def test_this():
    sl=ScanLogs(logs_location="C:\\data\\kronshtadt\\QA\\BL\\AutomationFrameworkDesign\\ext_tools\\apache-chainsaw-2.0.0-standalone\\apache-chainsaw-2.0.0\\bin\kd_LogFile.log")
    sl.scan_logs(pattern=".*WatchDogServer.*")
    return

if __name__=="__main__":
    test_this()
