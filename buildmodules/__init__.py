from __future__ import (absolute_import, division, print_function)


class BaseModule(object):
    '''
    Base Build Module
    '''
    def __init__(self, ctx):
        if not ctx:
            raise RuntimeError('Incorrect container context, %s' % ctx)
        self.ctx = ctx
        self.logger = ctx.get_logger(__name__)

    def preprocess(self, **kwargs):
        pass

    def process(self, **kwargs):
        pass

    def postprocess(self, **kwargs):
        pass

    def run(self, **kwargs):
        self.preprocess(**kwargs)
        self.process(**kwargs)
        self.postprocess(**kwargs)
