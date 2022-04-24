from time import strftime


def generate_formatted_timestamp():
    '''
    return current timestamp including (fraction of a) second
    :return:
    '''

    return strftime("[%m/%d/%Y %H:%M:%S]")
