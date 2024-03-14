import ncs

class Ericsson():

    @staticmethod
    def template_flat_l3vpn(endpoint):
        template = ncs.template.Template(endpoint)
        template.apply('cisco-flat-L3vpn-fp-ericsson-template', None)

    def conf_l3vpn(self, endpoint):
        self.log.info('Configuring Flat L3VPN/SR on Ericsson device {}'.format(endpoint.access_pe))
        Ericsson.template_flat_l3vpn(endpoint)

    def get_bgp_as_from_device(self, root, device):
        return next(iter(root.devices.device[device].config
                .contexts.context['local'].router.bgp)).bgp

    def check_if_interface_exists(self, root, endpoint,
                                service_interface_name, service_interface_id):
        self.log.info('Checking {} {} on Ericsson device {}'.format(
            service_interface_name, service_interface_id, endpoint.access_pe))

        interfaces = root.devices.device[endpoint.access_pe].config.interfaces.interface
        return bool(interfaces) and service_interface_id in interfaces


    def is_vrf_address_family_active(self, root, device, bgp_as_no, vrf_name):
        contexts = root.devices.device[device].config.contexts
        return vrf_name in contexts

    def get_vrf_rd(self, root, device, vrf_name):
        # Return RD from global VRF
        contexts = root.devices.device[device].config.contexts
        if vrf_name in contexts:
            return contexts[vrf_name].vpn_conf.vpn_val
        return None

    def get_bgp_vrf_rd(self, root, device, bgp_as_no, vrf_name):
        # Return RD from BGP VRF instance
        contexts = root.devices.device[device].config.contexts
        if vrf_name in contexts:
            return contexts[vrf_name].vpn_conf.vpn_val
        return None

    def get_interface_shutdown_template(self):
        return None

    def l3vpn_self_test(self, root, service, vrf_name, device, src, dst):
        self.log.info('Running L3vpn self test on Ercisson device {}'.format(device))
        return ("success", "Not Implemented")


    def __init__(self, log, root, service):
        self.log=log
        self.root=root
        self.service=service
