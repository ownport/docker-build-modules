from __future__ import (absolute_import, division, print_function)


def update_packages(ctx):
    '''
    Update Alpine repositoties
    '''
    return ctx.cmd('apk update')


def add_packages(ctx, packages):
    '''
    Add package(-s)
    '''
    if isinstance(packages, (list, tuple)):
        return ctx.cmd('apk add %s' % ' '.join(packages))
    else:
        raise RuntimeError('The packages list shall be list or tuple, founded: %s' % type(packages))


def remove_packages(ctx, packages):
    '''
    Remove package(-s)
    '''
    if isinstance(packages, (list, tuple)):
        return ctx.cmd('apk del %s' % ' '.join(packages))
    else:
        raise RuntimeError('The packages list shall be list or tuple, founded: %s' % type(packages))
