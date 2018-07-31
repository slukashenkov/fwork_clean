from test_bl.test_sonata_plugin.test_tools_sonata import sonata_test_parser

class SonataNmeaMsgsContentProcessing:
    def __init__(self,
                 data_from=None,
                 data_to=None
                 ):

        """
        :param data_from:
        :param data_to:
        """
        '''
        SETUP DATA to work on
        '''
        self.data_from=data_from
        self.data_to=data_to

        '''
        SETUP PROCESSED DATA 
        Storage  
        '''
        self.data_parsed = None

        '''
        PACKET PROCESSING INSTRUCTIONS
        only index FOR DEMO
        '''
        self.packet_indx = None

        '''
        Keys for comparisons 
        '''
        self.key_sent       = None
        self.key_received   = None

        '''
        TEMP debug  
        Thing!!!
        TODO: here should be processing 
        for all values in all iterables holding
        messages
        playing part in the particular test.
        Both outgoing and incoming.
        '''

        '''
        Initialize parser with data
        to parse
        '''
        self.nmea_parser=sonata_test_parser.SonataTestParser(self.data_from,
                                                             self.data_to
                                                            )
        return


    def parse_nmea(self):
        #self.curr_msg = self.data_from[0]
        #self.nmea_parser.data_from = self.curr_msg
        self.nmea_parser.packet_indx = self.packet_indx
        self.data_parsed = self.nmea_parser.parse_from()
        return

    def parse_sonata(self):
        self.nmea_parser.parse_to()
        return

    def compare_fields(self):
        self.nmea_parser.key_sent = self.key_sent
        self.nmea_parser.key_received = self.key_received
        self.nmea_parser.compare_fields()
        return

    def get_field_in(self):
        return self.data_parsed[self.key_received]

    def get_field_out(self):
        return self.data_to[self.key_sent]