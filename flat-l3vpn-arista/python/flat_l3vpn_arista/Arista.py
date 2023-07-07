import ncs

class Arista():

    @staticmethod
    def template_flat_l3vpn(endpoint):
        template = ncs.template.Template(endpoint)
        template.apply('cisco-flat-L3vpn-fp-arista-template', None)

    def conf_l3vpn(self, endpoint):
        self.log.info('Configuring Flat L3VPN/SR on Arista device {}'.format(endpoint.access_pe))
        Arista.template_flat_l3vpn(endpoint)


    def check_if_interface_exists(self, root, endpoint,
                                service_interface_name, service_interface_id):
        self.log.info('Checking {} {} on Arista device {}'.format(
            service_interface_name, service_interface_id, endpoint.access_pe))

        interfaces = root.devices.device[endpoint.access_pe].config.interface
        if service_interface_name == 'Loopback':
            interfaces = interfaces.Loopback
        else:
            interfaces = interfaces.Ethernet

        return bool(interfaces) and service_interface_id in interfaces


    def is_vrf_address_family_active(self, root, device, bgp_as_no, vrf_name):
        router = root.devices.device[device].config.router
        return bgp_as_no in router.bgp and vrf_name in router.bgp[bgp_as_no].vrf

    def get_vrf_rd(self, root, device, vrf_name):
        # Return RD from global VRF
        vrf_instances = root.devices.device[device].config.vrf.instance
        if vrf_name in vrf_instances:
            return vrf_instances[vrf_name].rd
        return None


    def get_bgp_vrf_rd(self, root, device, bgp_as_no, vrf_name):
        # Return RD from BGP VRF instance
        router = root.devices.device[device].config.router
        if bgp_as_no in router.bgp and vrf_name in router.bgp[bgp_as_no].vrf:
            return router.bgp[bgp_as_no].vrf[vrf_name].rd
        return None

    def get_interface_shutdown_template(self):
        return None

    def l3vpn_self_test(self, root, service, vrf_name, device, src, dst):
        self.log.info('Running L3vpn self test on Arista device {}'.format(device))
        return ("success", "Not Implemented")


    def __init__(self, log, root, service):
        self.log=log
        self.root=root
        self.service=service
