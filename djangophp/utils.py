import sys
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

from django.template import loader as django_template_loader
from django.conf import settings

import php

def find_template(name, dirs=None):
    if django_template_loader.template_source_loaders is None:
        loaders = []
        for loader_name in settings.TEMPLATE_LOADERS:
            loader = django_template_loader.find_template_loader(loader_name)
            if loader is not None:
                loaders.append(loader)
        django_template_loader.template_source_loaders = tuple(loaders)
    for loader in django_template_loader.template_source_loaders:
        try:
            source, display_name = loader.load_template_source(name, dirs)
            return source, display_name
        except django_template_loader.TemplateDoesNotExist:
            pass
    raise django_template_loader.TemplateDoesNotExist(name)

def run_php(filepath, *args, **kwargs):
    sio = StringIO()
    _tmp = sys.stdout
    sys.stdout = sio
    php.run(filepath, *args, **kwargs)
    sys.stdout = _tmp
    return sio.getvalue()
