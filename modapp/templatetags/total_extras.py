from django import template

NIS_SIGN = chr(8362)

register = template.Library()

@register.filter
def format_nis(value):
    """
    Formats the given value in NIS.
    :param value: Value to format, in agorot.
    :type value: int
    :return: Formatted value in NIS.
    :rtype: str
    """
    nis = str(value // 100)
    agorot = str(value % 100).zfill(2)
    return "%s.%s %s" % (nis, agorot, NIS_SIGN)
