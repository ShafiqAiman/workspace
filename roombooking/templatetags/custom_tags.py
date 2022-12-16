from django import template
from datetime import datetime

register = template.Library()

@register.filter
def convertToTime(value):
    return datetime.strptime(value, '%H:%M:%S').time()

@register.filter
def get_type(value):
    return type(value)

@register.simple_tag
def check_time_range(time, start_time, end_time):
    time = datetime.strptime(time, '%H:%M:%S').time()
    if start_time <= time <= end_time:
        return True
    return False