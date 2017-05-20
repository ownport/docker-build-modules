from __future__ import (absolute_import, division, print_function)

from buildmodules.alpine import utils
from buildmodules.alpine.v1 import BuildModule as AlpineBuildModule


class BuildModule(AlpineBuildModule):

    vars_prefix = __name__

    def process(self):
        '''
        Build docker image with python
        '''
        py_version = self.get_var('version', None)
        if py_version == 'py2':
            self._install_py2()
        elif py_version == 'py3':
            self._install_py3()
        else:
            raise RuntimeError('Unknown python version, %s' % py_version)

    def _install_py2(self):
        '''
        Build docker image with python3
        '''
        self.logger.info(msg='Install: python')
        utils.add_packages(self.ctx, ['python',])

        if self.get_var('install_pip', False):
            self.logger.info(msg='Install: python-pip')
            utils.add_packages(self.ctx, 'pip')

    def _install_py3(self):
        '''
        Build docker image with python3
        '''
        self.logger.info(msg='Install: python3')
        utils.add_packages(self.ctx, ['python3',])

        if self.get_var('install_pip', False):
            self.logger.info(msg='Install: python3-pip')
            utils.add_packages(self.ctx, 'py3-pip')
