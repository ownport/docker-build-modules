from __future__ import (absolute_import, division, print_function)

from buildmodules.alpine import utils
from buildmodules.alpine.v1 import BuildModule as AlpineBuildModule


class BuildModule(AlpineBuildModule):
    def process(self, **kwargs):
        '''
        Build docker image with python3
        '''
        self.logger.info(msg='Install: python3')
        utils.add_packages(self.ctx, ['python3',])

        if kwargs.get('%s.install_pip' % self.vars_prefix, False):
            self.logger.info(msg='Install: python3-pip')
            utils.add_packages(self.ctx, 'py3-pip')
