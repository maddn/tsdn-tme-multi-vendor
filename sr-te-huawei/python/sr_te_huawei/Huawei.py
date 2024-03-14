import ncs

class Huawei():

    @staticmethod
    def template_sr_policy(service, device):
        template = ncs.template.Template(service)
        template_vars = ncs.template.Variables()
        template_vars.add('HEAD_END',device)
        template.apply('cisco-sr-te-cfp-huawei-sr-policy', template_vars)

    def conf_segment_list(self, device):
        self.log.info('Segment list not supported on Huawei')

    def conf_sr_policy(self, device) :
        self.log.info(
            'Configuring sr-policy on Huawei device {}'.format(device))
        Huawei.template_sr_policy(self.service, device)

    def conf_sr_template(self, device):
        self.log.info('ODN not support on Huawei')

    def get_max_sid_depth(self, root, device):
        self.log.info('Max SID depth not support on Huawei')
        return None


    def __init__(self, log, root, service):
        self.log=log
        self.root=root
        self.service=service
