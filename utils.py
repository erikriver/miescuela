import os
from django.core.exceptions import ImproperlyConfigured

no_default_provided = dict()


def get_environ_setting(key, default=no_default_provided):
    """ Get the environment variable or raise exception """
    try:
        return os.environ[key]
    except KeyError:
        if default is no_default_provided:
            error_msg = "Set the %s environment variable" % key
            raise ImproperlyConfigured(error_msg)
        else:
            return default
