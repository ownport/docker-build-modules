from __future__ import (absolute_import, division, print_function)


class BaseModule(object):
    '''
    Base Build Module
    '''
    vars_prefix = __name__

    def __init__(self, ctx):
        if not ctx:
            raise RuntimeError('Incorrect container context, %s' % ctx)
        self.ctx = ctx
        self.logger = ctx.get_logger(__name__)
        self.kwargs = dict()

    def get_var(self, name, default_value=None, use_prefix=True):
        '''
        return variable value or default
        :param name: variable's name
        :param default_value: default value for variable if not exists
        :param use_prefix: use module path as prefix
        :return: the value of variable
        '''
        if use_prefix:
            name = "{}.{}".format(self.vars_prefix, name)
        return self.kwargs.get(name, default_value)

    def preprocess(self):
        pass

    def process(self):
        pass

    def postprocess(self):
        pass

    def run(self, **kwargs):
        if not isinstance(kwargs, dict):
            raise ValueError('Expected dict type for kwargs, found %s' % type(kwargs))
        self.kwargs = kwargs

        self.preprocess()
        self.process()
        self.postprocess()
