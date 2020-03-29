from trex.emu.api import *
from trex.emu.emu_plugins.emu_plugin_base import *
import trex.utils.parsing_opts as parsing_opts
import json


class DHCPPlugin(EMUPluginBase):
    '''Defines DHCP plugin'''

    plugin_name = 'DHCP'

    # init jsons example for SDK
    INIT_JSON_NS = {'dhcp': {}}
    """
    :parameters:
        Empty.
    """

    INIT_JSON_CLIENT = {'dhcp': {'timerd': 5, 'timero': 10}}
    """
    :parameters:
        timerd: uint32
            DHCP timer discover in sec.
        timero: uint32
            DHCP timer offer in sec.
    """

    def __init__(self, emu_client):
        super(DHCPPlugin, self).__init__(emu_client, 'dhcp_client_cnt')

    # Plugins methods

    @plugin_api('dhcp_show_counters', 'emu')
    def dhcp_show_counters_line(self, line):
        '''Show dhcp counters (per client).\n'''
        parser = parsing_opts.gen_parser(self,
                                        "show_counters_dhcp",
                                        self.dhcp_show_counters_line.__doc__,
                                        parsing_opts.EMU_SHOW_CNT_GROUP,
                                        parsing_opts.EMU_NS_GROUP,
                                        parsing_opts.EMU_CLIENT_GROUP,
                                        parsing_opts.EMU_DUMPS_OPT
                                        )

        opts = parser.parse_args(line.split())
        self.emu_c._base_show_counters(self.data_c, opts, req_ns = True)
        return True