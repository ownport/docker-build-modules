from __future__ import (absolute_import, division, print_function)

from buildmodules import BaseModule
from buildmodules.alpine.utils import update_packages


class BuildModule(BaseModule):
    '''
    Alpine Build Module
    '''
    vars_prefix = __name__

    def preprocess(self):
        self.logger.info(msg='Updating Alpine repositories')
        update_packages(self.ctx)

    def postprocess(self):
        # Cleaning Alpine repositories cache
        if self.get_var('clean_cache', True):
            self.logger.info(msg='Cleaning Alpine repositories cache')
            self.ctx.cmd('find /var/cache/apk/ -type f -delete')
