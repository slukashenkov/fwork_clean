import logging
from test_bl.test_sonata_plugin.configs_sonata import sonata_send_recieve_properties, sonata_suite_config
from test_bl_tools.scan_logs import ScanLogs

class SonataTestParser:
    def __init__(self,
                 conf = None,
                 data_from=None,
                 data_to=None
                 ):
        """

        :param data_from:
        :param data_to:
        """
        self.range = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        '''
        LETS NOT DO ANYTHING WITHOUT PROPER LOGGER
        '''
        if conf == None:
            raise Exception("Test suite config is not provived. \n CAN NOT LOG ANYTHING HERE!")

        else:
            '''
            SetUp logger
            '''
            self.conf = conf
            self.logger = self.conf.logging_tools.get_logger(__name__)

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
        self.sonata_nmea_parsed_map = {}
        self.sonata_nmea_to = {}
        return

        '''
        SPECIFIC VALUES TO COMPARE
        '''
        self.key_sent = None
        self.key_received = None

        '''
        SETUP FOR LOG FILE RAKING
        '''
        self.log_dir_name




    def parse_from(self):
        """
        :return:
        """
        '''
        GET PARTICULAR PAKET
        by index
        '''
        try:
            self.data_from[self.packet_indx]
        except IndexError:
            self.logger.info("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            self.logger.info("No RETURN packet FOUND at the index: "+ str(self.packet_indx) + " IN THE DATA_FROM STRUCTURE")
            self.logger.info("BL/MUSSON CAN BE DOWN AT THE MOMENT")
            self.logger.info("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

            raise Exception("NO PACKETS GOTTEN FROM BL FOR PROCESSING. So IT SEEMS.")

        data_to_parse = self.data_from[self.packet_indx]

        print(data_to_parse)
        ind_values=data_to_parse.split(",")

        indx = 0
        lat = {}
        lon = {}
        vel = {}
        course = {}
        data_from = {}
        data_from["lat"] = lat
        data_from["lon"] = lon
        data_from["vel"] = vel
        data_from["course"] = course

        for val in ind_values:
            if val:
                label = "label" + str(indx)
                self.sonata_nmea_from[label] = val
                if indx == 2:
                    data_from["sonata_id"] = val
                    indx += 1
                    continue
                if indx == 6:
                    course["deg"] = val
                    course["tens_deg"] = val
                    indx += 1
                    continue
                if indx == 10:
                    data_from["vel_knots"] = val
                    indx += 1
                    continue
                if indx == 14:
                    vel["hkm_h"] = val
                    vel["km_h"] = val
                    indx += 1
                    continue
                if indx == 18:
                    lat["deg"] = val
                    lat["min"] = val
                    lat["sec"] = val
                    lat["tens_sec"] = val
                    indx += 1
                    continue

                if indx == 26:
                    lon["deg"] = val
                    lon["min"] = val
                    lon["sec"] = val
                    lon["tens_sec"] = val
                    indx += 1
                    continue

            indx += 1

        self.sonata_nmea_parsed_map = data_from
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

    def compare_fields(self,
                        sonata_id   =   None,
                        lat         =   None,
                        lon         =   None,
                        vel         =   None,
                        vel_knots   =   None,
                        course      =   None
                        ):

        result = False

        if sonata_id != None and  ((sonata_id in self.data_to) and (sonata_id in self.sonata_nmea_from_parsed)):
            field_sent = self.data_to[sonata_id]
            field_received = int(self.sonata_nmea_from_parsed[sonata_id])
            try:
                assert field_sent == field_received, "Fields ARE NOT equal"
                result = True
                self.logger.info("Comparison of "+ str(field_sent)  +" and " + str(field_received) + " in field named: "+ " was successful")
                return result
            except:
                self.logger.info("Comparison of " + str(field_sent) + " and " + str(field_received) + " in field named: " + sonata_id + " FAILED MISERABLY")
                return result

        if lat != None and  ((lat in self.data_to) and (lat in self.sonata_nmea_from_parsed)):
            field_sent = self.data_to[lat]
            field_sent_str = str(field_sent["deg"]) + str(field_sent["min"]) + str(field_sent["sec"])+"." + str(field_sent["tens_sec"])
            field_received=self.sonata_nmea_from_parsed[lat]["deg"]
            try:
                assert field_sent_str==field_received, "Fields ARE NOT equal"
                result = True
                self.logger.info("Comparison of " + field_sent_str + " and " + field_received + " in field named: " + " was successful")
                return result
            except:
                self.logger.info("Comparison of " + field_sent_str + " and " + field_received + " in field named: " + lat + " FAILED MISERABLY")
                return result

        if lon != None and  ((lon in self.data_to) and (lon in self.sonata_nmea_from_parsed)):
            field_sent = self.data_to[lon]
            field_sent_str = str(field_sent["deg"])+str(field_sent["min"])+str(field_sent["sec"])+"."+str(field_sent["tens_sec"])
            field_received=self.sonata_nmea_from_parsed[lon]

            field_received = self.sonata_nmea_from_parsed[lon]["deg"]
            try:
                assert field_sent_str == field_received, "Fields ARE NOT equal"
                result = True
                self.logger.info("Comparison of " + field_sent_str + " and " + field_received+ " in field named: " + lon + " was successful")
                return result
            except:
                self.logger.info("Comparison of " + field_sent_str + " and " + field_received + " in field named: " + lon + " FAILED MISERABLY")
                return result

        if vel != None and  ((vel in self.data_to) and (vel in self.sonata_nmea_from_parsed)):
            field_sent = self.data_to[vel]
            '''
            if (field_sent["hkm_h"] or field_sent["km_h"]) in self.range:
                field_sent_hkm_h_str = str(0) + str(field_sent["hkm_h"])
                field_sent_km_h_str = str(0) + str(field_sent["km_h"])
                field_sent_str = field_sent_hkm_h_str + field_sent_km_h_str
            else:
                field_sent_str = str(field_sent["hkm_h"]) + str(field_sent["km_h"])
            '''
            field_sent_str = str(field_sent["hkm_h"]) + str(field_sent["km_h"])
            field_received=self.sonata_nmea_from_parsed[vel]["hkm_h"]
            try:
                assert field_sent_str == field_received, "Fields ARE NOT equal"
                result = True
                self.logger.info("Comparison of " + field_sent_str + " and " + field_received + " in field named: " + vel + " was successful")
                return result
            except:
                self.logger.info("Comparison of " + field_sent_str + " and " + field_received + " in field named: " + vel + " FAILED MISERABLY")
                return result


        if course != None and  ((course in self.data_to) and (course in self.sonata_nmea_from_parsed)):
            field_sent = self.data_to[course]
            field_sent_str = str(field_sent["deg"]) + str(field_sent["tens_deg"])

            field_received=self.sonata_nmea_from_parsed[course]["deg"]
            try:
                assert field_sent_str == field_received, "Fields ARE NOT equal"
                result = True
                self.logger.info("Comparison of " + field_sent_str + " and " + field_received+ " in field named: " + course + " was successful")
                return result
            except:
                self.logger.info("Comparison of " + field_sent_str + " and " + field_received + " in field named: " + course +" FAILED MISERABLY")
                return result



        if vel_knots != None and vel_knots in self.sonata_nmea_from_parsed:
            field_sent = self.data_to["vel"]
            field_sent_str_hkm_h = str(field_sent["hkm_h"])
            field_sent_str_hkm_h = float(field_sent_str_hkm_h)*100
            field_sent_str_km_h = str(field_sent["km_h"])
            field_sent_str_km_h = float(field_sent_str_km_h)

            field_sent_calc = field_sent_str_hkm_h + field_sent_str_km_h
            field_sent_calc = field_sent_calc / 1.852
            field_sent_calc = round(field_sent_calc)
            field_sent_str = str(field_sent_calc)

            field_received = self.sonata_nmea_from_parsed[vel_knots]
            field_received = float(field_received)
            field_received = round(field_received)


            try:
                #assert field_sent_str == field_received, "Fields ARE NOT equal"
                assert str(field_sent_calc) == str(field_received), "Fields ARE NOT equal"
                result = True
                self.logger.info("Comparison of " + str(field_sent) + " " + field_sent_str + " " + str(field_sent_calc)+ " and " + str(field_received) + " in field named: " + vel_knots + " was successful")
                return result
            except:
                self.logger.info("Comparison of " +str(field_sent) + " " + field_sent_str +" " + str(field_sent_calc) + " and " + str(field_received) + " in field named: " + vel_knots + " FAILED MISERABLY")
                return result

        self.logger.info("Comparison of WAS NOT TRIGGERED FOR ANY CONDITION.Something is OFF")
        return result


    def parse_log(self,
                  pattern_in = None):
        search_substr = ScanLogs(conf_in = self.conf)
        log_location = self.conf.bl_log_dir

        if pattern_in != None:
            result = search_substr.scan_logs(pattern_in)
        else:
            raise Exception ("NO PATTERN TO SEARCH FOR")
        return result

    def parse_log_auto(self):

        '''For each element sent test for substring'''
        pattern_in = []
        try:
            for i in self.conf.data_sent_list:
                if i["fail"] != "":
                    pattern_in.append(i["log_pttrn"])

        except:
            raise Exception("Something is wrong with our assumption that we can iterate over sent messages list")

        try:
            for pattern in pattern_in:
                search_substr = ScanLogs(conf_in=self.conf)
                log_location = self.conf.bl_log_dir

                if pattern != "":
                    result = search_substr.scan_logs(pattern)
                else:
                    raise Exception("NO PATTERN TO SEARCH FOR")
                return result
        except:
            raise Exception("Something is wrong with our assumption that we formed a list of patterns")
        return