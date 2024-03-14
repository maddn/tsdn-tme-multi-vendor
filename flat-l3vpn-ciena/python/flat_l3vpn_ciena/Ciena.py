import ncs

class Ciena():
    @staticmethod
    def template_flat_l3vpn(endpoint, as_no):
        template = ncs.template.Template(endpoint)
        l3vpn_vars = ncs.template.Variables()
        l3vpn_vars.add("AS_NO", as_no)
        template.apply('cisco-flat-L3vpn-fp-ciena-template', l3vpn_vars)

    def conf_l3vpn(self, endpoint):
        self.log.info('Configuring Flat L3VPN/SR on Ciena device {}'.format(endpoint.access_pe))
        as_no = ''
        if endpoint.as_no is not None:
            as_no = endpoint.as_no
        elif endpoint.as_no_from_device.exists():
            as_no = self.get_bgp_as_from_device(self.root, endpoint.access_pe)
        Ciena.template_flat_l3vpn(endpoint, as_no)

    def get_bgp_as_from_device(self, root, device):
        return ncs.maagic.cd(next(iter(root.devices.device[device].config
                .bgp.instance)), 'as')

    def check_if_interface_exists(self, root, endpoint,
                                service_interface_name, service_interface_id):
        self.log.info('Checking {} {} on Ciena device {}'.format(
            service_interface_name, service_interface_id, endpoint.access_pe))

        interfaces = root.devices.device[endpoint.access_pe].config.oc_if__interfaces.interface
        return bool(interfaces) and service_interface_id in interfaces


    def is_vrf_address_family_active(self, root, device, bgp_as_no, vrf_name):
        vrfs = root.devices.device[device].config.bgp.instance[bgp_as_no].vrf
        return vrf_name in vrfs

    def get_vrf_rd(self, root, device, vrf_name):
        # Return RD from global VRF
        return None

    def get_bgp_vrf_rd(self, root, device, bgp_as_no, vrf_name):
        # Return RD from BGP VRF instance
        vrfs = root.devices.device[device].config.bgp.instance[bgp_as_no].vrf
        if vrf_name in vrfs:
            return vrfs[vrf_name].route_distinguisher
        return None

    def get_interface_shutdown_template(self):
        return None

    def l3vpn_self_test(self, root, service, vrf_name, device, src, dst):
        self.log.info('Running L3vpn self test on Ciena device {}'.format(device))
        return ("success", "Not Implemented")


    def __init__(self, log, root, service):
        self.log=log
        self.root=root
        self.service=service
