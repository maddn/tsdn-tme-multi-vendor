import ncs

class Huawei:
    def conf_l2vpn(self, site, local):
        self.log.info(f"Configuring Flat L2VPN/SR on Huawei for service {site.pe}")

        l2vpn_vars = ncs.template.Variables()
        l2vpn_template = ncs.template.Template(site)

        if self.service.service_type == "evpn-vpws":
            l2vpn_vars.add("LOCAL_NODE", "true" if local is True else "false")
            l2vpn_template.apply("cisco-flat-L2vpn-fp-huawei-p2p-template", l2vpn_vars)
        elif self.service.service_type == "evpn-multipoint":
            l2vpn_template.apply("cisco-flat-L2vpn-fp-huawei-mp-template", l2vpn_vars)

    def conf_l2vpn_rp(self, rr_parent_route_policy):
        self.log.info("Route Policy is currently not supported on Huawei, passing")

    def validate_parent_policy_exists(self, root, device, parent_policy):
        self.log.info("Route Policy is currently not supported on Huawei, passing")
        return True

    def get_original_policy(self, root, device, parent_policy):
        self.log.info("Route Policy is currently not supported on Huawei, passing")
        return ""

    def check_if_interface_exists(self, root, site,
                                service_interface_name, service_interface_id):
        interface_name = '{}{}'.format(
            service_interface_name, service_interface_id)

        self.log.info('Checking {} on Huawei device {}'.format(
            interface_name, site.pe))
        interfaces = root.devices.device[site.pe].config.interfaces.interface

        return bool(interfaces) and interface_name in interfaces

    def get_interface_shutdown_template(self):
        return None

    def l2vpn_self_test(self, root, service, device, xc_group, xc_name):
        self.log.info(f"Running L2vpn self test on Huawei device {device}")
        return ("success", "Not Implemented")


    def __init__(self, log, root, service):
        self.log = log
        self.root = root
        self.service = service
