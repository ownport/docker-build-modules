from __future__ import (absolute_import, division, print_function)

from buildmodules.alpine import utils
from buildmodules.alpine.v1 import BuildModule as AlpineBuildModule


class BuildModule(AlpineBuildModule):
    def process(self, **kwargs):
        '''
        Build docker image with python
        '''
        self.logger.info(msg='Install: python')
        utils.add_packages(self.ctx, ['python',])

        if kwargs.get('%s.install_pip' % self.vars_prefix, False):
            self.logger.info(msg='Install: python-pip')
            utils.add_packages(self.ctx, 'pip')
