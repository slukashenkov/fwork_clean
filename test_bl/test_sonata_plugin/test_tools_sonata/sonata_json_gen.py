from mimesis.schema import Field, Schema
from mimesis import Generic
import json

class SonataJsonDataGen():
    def __init__(self,
                 gen_file_dir = 'C:\\data\\kronshtadt\\QA\\BL\\AutomationFrameworkDesign\\bl_frame_work\\test_bl\\test_sonata_plugin\\resources_sonata',
                 gen_file_name = 'sonata_gen_data.json'):
        self.g_provider = Generic('en')
        num = self.g_provider.numbers.between(
                                            minimum=0,
                                            maximum=365
                                            )
        _ = Field('en')
        self.sonata_msg_json = (
            lambda: {
                "mtype": _('numbers.between', minimum=0,
                                              maximum=3),

                "sonata_id": _('numbers.between', minimum=0,
                                                  maximum=4095),
                "lat": {
                    "deg": _('numbers.between', minimum=0,
                                                  maximum=4095),
                    "min": _('numbers.between', minimum=0,
                                                  maximum=4095),
                    "sec": _('numbers.between', minimum=0,
                                                  maximum=4095),
                    "tens_sec": _('numbers.between', minimum=0,
                                                  maximum=4095)
                },



                "lon": {
                    "deg": _('numbers.between', minimum=0,
                                                  maximum=4095),
                    "min": _('numbers.between', minimum=0,
                                                  maximum=4095),
                    "sec": _('numbers.between', minimum=0,
                                                  maximum=4095),
                    "tens_sec": _('numbers.between', minimum=0,
                                                  maximum=4095)
                },
                "vel": {"hkm_h": _('numbers.between', minimum=0,
                                                  maximum=1),
                        "km_h": _('numbers.between', minimum=0,
                                                  maximum=99)
                        },
                "course": {
                    "deg": _('numbers.between', minimum=0,
                                                  maximum=99),
                    "tens_deg": _('numbers.between', minimum=0,
                                                  maximum=99)
                },
                "state": _('numbers.between', minimum=0,
                                                  maximum=99),
                "tail": _('numbers.between', minimum=0,
                                                  maximum=99),
                "signal_lvl": _('numbers.between', minimum=0,
                                                  maximum=99)


            }

        )
        self.sonata_schema = Schema(schema=self.sonata_msg_json)
        sonata_obj = self.sonata_schema.create(iterations=1)
        for i in sonata_obj:
            sonata_json = json.dumps(obj=i)

        pass

    def generate_sonata_json(self):
        return


def test_this():
    from mimesis.schema import Field, Schema

    s_json_gen = SonataJsonDataGen()



if __name__ == '__main__':
    test_this()