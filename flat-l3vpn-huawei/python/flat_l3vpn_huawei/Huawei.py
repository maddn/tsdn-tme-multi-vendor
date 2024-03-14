import ncs

class Huawei():

    @staticmethod
    def template_flat_l3vpn(endpoint):
        template = ncs.template.Template(endpoint)
        template.apply('cisco-flat-L3vpn-fp-huawei-template', None)

    def conf_l3vpn(self, endpoint):
        self.log.info('Configuring Flat L3VPN/SR on Huawei device {}'.format(endpoint.access_pe))
        Huawei.template_flat_l3vpn(endpoint)

    def get_bgp_as_from_device(self, root, device):
        return root.devices.device[device].config.bgp.base_process['as']

    def check_if_interface_exists(self, root, endpoint,
                                service_interface_name, service_interface_id):
        self.log.info('Checking {} {} on Huawei device {}'.format(
            service_interface_name, service_interface_id, endpoint.access_pe))

        interface_mapping = {
            'GigabitEthernet':  'GigabitEthernet',
            'TwentyFiveGigE':   '25GE',
        }

        interface_name = '{}{}'.format(
            interface_mapping[service_interface_name], service_interface_id)

        interfaces = root.devices.device[endpoint.access_pe].config.ifm__ifm.interfaces.interface
        return bool(interfaces) and interface_name in interfaces

    def is_vrf_address_family_active(self, root, device, bgp_as_no, vrf_name):
        instances = root.devices.device[device
                ].config.huawei_ni__network_instance.instances.instance
        return vrf_name in instances

    def get_vrf_rd(self, root, device, vrf_name):
        # Return RD from global VRF
        instances = root.devices.device[device
                ].config.huawei_ni__network_instance.instances.instance
        if vrf_name in instances:
            return instances[vrf_name].afs.af['ipv4-unicast'].route_distinguisher
        return None

    def get_bgp_vrf_rd(self, root, device, bgp_as_no, vrf_name):
        # Return RD from BGP VRF instance
        return None

    def get_interface_shutdown_template(self):
        return None

    def l3vpn_self_test(self, root, service, vrf_name, device, src, dst):
        self.log.info('Running L3vpn self test on Huawei device {}'.format(device))
        return ("success", "Not Implemented")


    def __init__(self, log, root, service):
        self.log=log
        self.root=root
        self.service=service
