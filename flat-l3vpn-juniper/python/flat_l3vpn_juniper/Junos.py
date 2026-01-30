import ncs

class Junos():

    @staticmethod
    def template_flat_l3vpn(endpoint):
        template = ncs.template.Template(endpoint)
        template.apply('cisco-flat-L3vpn-fp-junos-template', None)

    def conf_l3vpn(self, endpoint):
        self.log.info('Configuring Flat L3VPN/SR on Junos device {}'.format(endpoint.access_pe))
        Junos.template_flat_l3vpn(endpoint)

    def get_bgp_as_from_device(self, root, device):
        return (root.devices.device[device].config.junos__configuration
                .routing_options.autonomous_system.as_number)

    def check_if_interface_exists(self, root, endpoint,
                                service_interface_name, service_interface_id):
        interface_mapping = {
            'Bundle-Ether':     'ae',
            'BVI':              'irb',
            'Ethernet':         'fe',
            'FiftyGigE':        'et',
            'FortyGigE':        'et',
            'FourHundredGigE':  'et',
            'GigabitEthernet':  'ge',
            'HundredGigE':      'et',
            'Loopback':         'lo',
            'TenGigE':          'xe',
            'TwentyFiveGigE':   'et',
            'TwoHundredGigE':   'et'
        }

        interface_name = '{}-{}'.format(
            interface_mapping[service_interface_name], service_interface_id)

        self.log.info('Checking {} on Junos device {}'.format(
            interface_name, endpoint.access_pe))

        device_interfaces = (root.devices.device[endpoint.access_pe].config
                             .configuration.interfaces.interface)

        return bool(device_interfaces) and interface_name in device_interfaces


    def is_vrf_address_family_active(self, root, device, bgp_as_no, vrf_name):
        routing_instances = (root.devices.device[device].config.configuration
                             .routing_instances.instance)
        return (vrf_name in routing_instances and
                routing_instances[vrf_name].routing_options.autonomous_system
                    .as_number == bgp_as_no)


    def get_vrf_rd(self, root, device, vrf_name):
        # Return RD from global VRF
        routing_instances = (root.devices.device[device].config.configuration
                             .routing_instances.instance)
        if vrf_name in routing_instances:
            return routing_instances[vrf_name].route_distinguisher.rd_type
        return None


    def get_bgp_vrf_rd(self, root, device, bgp_as_no, vrf_name):
        # Return RD from BGP VRF instance
        return None

    def get_interface_shutdown_template(self):
        return None

    def validate_vlan_id_exists(self, root, device, vlan_id,
            service_interface_name, service_interface_id, vrf_name):
        interface_name = '{}-{}.{}'.format(
            Junos.interface_mapping[service_interface_name], service_interface_id, vlan_id)

        routing_instances = (root.devices.device[device].config.configuration
                             .routing_instances.instance)

        for instance in routing_instances:
            if instance.interface.name == interface_name and instance.name != vrf_name:
                self.log.debug(f"detected vlan overlap for {interface_name} in VRF {instance.name}")
                return True
        return False

    def l3vpn_self_test(self, root, service, vrf_name, device, src, dst):
        self.log.info('Running L3vpn self test on Junos device {}'.format(device))
        return ("success", "Not Implemented")


    def __init__(self, log, root, service):
        self.log=log
        self.root=root
        self.service=service
