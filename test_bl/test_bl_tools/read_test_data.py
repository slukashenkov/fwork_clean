import json
from test_bl.test_sonata_plugin.configs_sonata import sonata_send_recieve_properties

class ReadData:
    def __init__(self,
                 data_location_map="C:\\data_from\\kronshtadt\\QA\\BL\\AutomationFrameworkDesign\\bl_frame_work\\test_bl\\test_sonata_plugin\\resources_sonata\\sonata_fields",
                 data_location_list="C:\\data_from\\kronshtadt\\QA\\BL\\AutomationFrameworkDesign\\bl_frame_work\\test_bl\\test_sonata_plugin\\resources_sonata\\sonata_fields"
                 ):
        self.data_location_map = data_location_map
        self.data_location_list = data_location_list
        self.final_map=None
        self.final_list = None
        return

    def read_file_to_map(self):
        map = {}
        with open(self.data_location_map) as f:
            for line in f:
                (key, val) = line.split()
                map[key] = val
        self.final_map=map
        return

    def read_file_to_list(self):
        list = []
        with open("file.txt") as f:
            for line in f:
                (key, val) = line.split()
                list.append(val)
        self.final_list = list
        return

    def read_json_to_map(self):
        with open(self.data_location_map, "r") as read_file:
            map = json.load(read_file)
            self.final_map = map
        return

    def read_json_to_list(self):
        return


if __name__ == '__main__':
    """
       BASIC TEST BASIC CONFIG
       """
    # conf=sonata_send_recieve_properties.SonataSendReceiveProperties()
    # rd = ReadData(conf.def_mgs_location)
    # rd.read_file_to_map()
    '''
    Read test data from json
    '''
    #def_mgs_location = "D:\\data\\python\\projects\\bl_frame_work\\bl_frame_work\\test_bl\\test_sonata_plugin\\resources_sonata\sonata_test_data.json"
    def_mgs_location = "C:\\data\\kronshtadt\\QA\\BL\\AutomationFrameworkDesign\\bl_frame_work\\test_bl\\test_sonata_plugin\\resources_sonata\\sonata_test_data.json"
    rd = ReadData(def_mgs_location)
    rd.read_json_to_map()
    print("End of test read data_from")