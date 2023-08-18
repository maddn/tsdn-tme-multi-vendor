import ncs

class Junos:
    def conf_l2vpn(self, site, local):
        self.log.info(f"Configuring Flat L2VPN/SR on Junos for service {site.pe}")

        if self.service.service_type == "evpn-vpws":
            l2vpn_vars = ncs.template.Variables()
            l2vpn_vars.add("LOCAL_NODE", "true" if local is True else "false")
            l2vpn_template = ncs.template.Template(site)
            l2vpn_template.apply("cisco-flat-L2vpn-fp-junos-template", l2vpn_vars)

    def conf_l2vpn_rp(self, rr_parent_route_policy):
        self.log.info("Route Policy is currently not supported on Junos, passing")

    def validate_parent_policy_exists(self, root, device, parent_policy):
        self.log.info("Route Policy is currently not supported on Junos, passing")
        return True

    def get_original_policy(self, root, device, parent_policy):
        self.log.info("Route Policy is currently not supported on Junos, passing")
        return ""

    def check_if_interface_exists(self, root, site,
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
            interface_name, site.pe))

        device_interfaces = (root.devices.device[site.pe].config
                             .configuration.interfaces.interface)

        return bool(device_interfaces) and interface_name in device_interfaces


    def get_interface_shutdown_template(self):
        return None

    def l2vpn_self_test(self, root, service, device, xc_group, xc_name):
        self.log.info(f"Running L2vpn self test on Junos device {device}")
        return ("success", "Not Implemented")


    def __init__(self, log, root, service):
        self.log = log
        self.root = root
        self.service = service
