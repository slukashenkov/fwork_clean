
class SonataTestParser:
    def __init__(self,
                 data_from=None,
                 data_to=None
                 ):
        """

        :param data_from:
        :param data_to:
        """

        '''
        ALL DATA TO PROCESS
        '''
        self.data_from = data_from
        self.data_to = data_to

        '''
        SPECIFIC PACKETS TO PROCESS
        '''
        self.packet_indx = None

        '''
        RESULTING STORAGE DATA STRUCTURES
        '''
        self.sonata_nmea_from = {}
        self.sonata_nmea_to = {}
        return

        '''
        SPECIFIC VALUES TO COMPARE
        '''
        self.key_sent = None
        self.key_received = None


    def parse_from(self):
        """
        :return:
        """
        '''
        GET PARTICULAR PAKET
        by index
        '''
        data_to_parse = self.data_from[self.packet_indx]

        print(data_to_parse)
        ind_values=data_to_parse.split(",")

        indx = 0
        for val in ind_values:
            if val:
                label = "label" + str(indx)
                self.sonata_nmea_from[label] = val
                indx += 1
        return self.sonata_nmea_from

    '''
    TODO or Not TODO AS it is not clear whether it is going to be needed at all
    BUT may ....
    in case when it is easier to store data unstructured and send it as-is
    and so parsing after the fact may be an option
    '''
    def parse_to(self):
        print(self.data_to)
        ind_values = self.data_to.split(",")

        indx = 0
        for val in ind_values:
            if val:
                label = "label" + str(indx)
                self.sonata_nmea_from[label] = val
                indx += 1
        return

    def compare_fields(self):
        field_sent = self.data_to[self.key_sent]
        field_received=self.sonata_nmea_from[self.key_received]

        if field_sent == field_received:
            return True
        else:
            return False