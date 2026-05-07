import ncs

class Nokia():

    @staticmethod
    def template_flat_l3vpn(endpoint):
        template = ncs.template.Template(endpoint)
        template.apply('cisco-flat-L3vpn-fp-nokia-template', None)

    def conf_l3vpn(self, endpoint):
        self.log.info('Configuring Flat L3VPN/SR on Nokia device {}'.format(endpoint.access_pe))
        Nokia.template_flat_l3vpn(endpoint)

    def get_bgp_as_from_device(self, root, device):
        return None

    def check_if_interface_exists(self, root, endpoint,
                                service_interface_name, service_interface_id):

        self.log.info('Checking {} on Nokia device {}'.format(
            service_interface_name, endpoint.access_pe))

        device_interfaces = root.devices.device[endpoint.access_pe].config.configure

        if service_interface_name == 'Bundle-Ether':
            return bool(device_interfaces.lag) and 'lag-{}'.format(
                    service_interface_id) in device_interfaces.lag

        return bool(device_interfaces.port) and (
                service_interface_id in device_interfaces.port)


    def is_vrf_address_family_active(self, root, device, bgp_as_no, vrf_name):
        return False


    def get_vrf_rd(self, root, device, vrf_name):
        # Return RD from global VRF
        return None


    def get_bgp_vrf_rd(self, root, device, bgp_as_no, vrf_name):
        # Return RD from BGP VRF instance
        return None

    def get_interface_shutdown_template(self):
        return None

    def validate_vlan_id_exists(self, root, device, vlan_id,
            service_interface_name, service_interface_id, vrf_name):
        return False

    def validate_srv6_te(self, root, service, device):
        pass

    def l3vpn_self_test(self, root, service, vrf_name, device, src, dst):
        self.log.info('Running L3vpn self test on Nokia device {}'.format(device))
        return ("success", "Not Implemented")


    def __init__(self, log, root, service):
        self.log=log
        self.root=root
        self.service=service
