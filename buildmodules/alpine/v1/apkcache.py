from __future__ import (absolute_import, division, print_function)

from buildmodules.alpine.v1 import BuildModule as AlpineBuildModule


class BuildModule(AlpineBuildModule):

    def process(self, **kwargs):
        # TODO commented due to using docker volumes for caching Alpine packages
        # self.logger.info(msg='Configuring Alpine cache components')
        # self.ctx.cmd('ln -s /var/cache/apk /etc/apk/cache')

        self.logger.info(msg='Sync Alpine packages with cache')
        self.ctx.cmd('apk cache sync')
