import ncs

class Junos():

    @staticmethod
    def template_sr_segment_list(service, device):
        template = ncs.template.Template(service)
        template_vars = ncs.template.Variables()
        template_vars.add('DEVICE', device)
        template.apply('cisco-sr-te-cfp-junos-segment-list', template_vars)

    @staticmethod
    def template_static_lsp(service, device):
        template = ncs.template.Template(service)
        template_vars = ncs.template.Variables()
        template_vars.add('HEAD_END',device)
        template.apply('cisco-sr-te-cfp-junos-static-lsp', template_vars)

    @staticmethod
    def template_dynamic_lsp(service, device):
        template = ncs.template.Template(service)
        template_vars = ncs.template.Variables()
        template_vars.add('HEAD_END', device)
        template.apply('cisco-sr-te-cfp-junos-dynamic-lsp', template_vars)


    def conf_segment_list(self, device):
        self.log.info(
            'Configuring segment-list on Junos device {}'.format(device))
        Junos.template_sr_segment_list(self.service, device)

    def conf_sr_policy(self, device) :
        self.log.info(
            'Configuring source-routing-path on Junos device {}'.format(device))
        Junos.template_static_lsp(self.service, device)

    def conf_sr_template(self, device):
        self.log.info(
            'Configuring source-routing-path-template on Junos device {}'
            .format(device))
        Junos.template_dynamic_lsp(self.service, device)


    def get_max_sid_depth(self, root, device):
        self.log.info('Getting max-sid-depth on Junos device {}'.format(device))
        pce_list = root.devices.device[device].config.\
                   junos__configuration.protocols.pcep.pce
        return next(iter(pce_list)).max_sid_depth if pce_list else 5


    def __init__(self, log, root, service):
        self.log=log
        self.root=root
        self.service=service
