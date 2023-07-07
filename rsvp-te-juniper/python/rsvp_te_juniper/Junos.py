import ncs

# ------------------------
# PLUG-In CLASS has to implement all funtions mentioned below
# ------------------------


class Junos:
    def get_interface_loopback(self, root, service):
        """
        Gets interface Loopback on given head-end

        """
        self.log.info(f"Find Loopback interface on {service.head_end}")
        return 0

    def conf_rsvp_te_tunnel_p2p(self, service, loopback):
        """
        Applies RSVP-TE config on the device.
        Path: /cisco-rsvp-te-fp:rsvp-te/tunnel-te
        """
        template = ncs.template.Template(service)
        template.apply("juniper-rsvp-te-template", None)
        self.log.info(f"Configuring RSVP TE on Junos device {service.head_end}")

    def ietf_te_self_test(self, uinfo, root, rsvp_te_service):
        """
        This method is run for RSVP-TE tunnel.
        It checks admin & operational state of the tunnel.
            Response should be either of these:
            ("success", None)
            ("failed", "some failure message")
        """
        self.log.info(f"Executing self-test on Junos device {rsvp_te_service.head_end}")

    def __init__(self, log, root, service):
        self.log = log
        self.root = root
        self.service = service
