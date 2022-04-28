import sys
from time import strftime


def generate_formatted_timestamp():
    '''
    return current timestamp including (fraction of a) second
    :return:
    '''

    return strftime("[%m/%d/%Y %H:%M:%S]")


def on_platforms(platforms):
    '''
    pass multiple platform configurations to be run in a single pass
    '''

    def decorator(base_class):
        module = sys.modules[base_class.__module__].__dict__
        for i, platform in enumerate(platforms):
            d = dict(base_class.__dict__)
            d['desired_capabilities'] = platform
            name = "%s_%s" % (base_class.__name__, i + 1)
            module[name] = type(name, (base_class,), d)
    return decorator


def generate_string_formatted_date():
    """ return date output in the form of Apr 25, 2022 """
    return strftime("%b %d, %Y")
