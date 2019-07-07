from datetime import datetime, timedelta

def half_birthday(birthday):
    """Returns a date 6 months later"""
    return birthday + timedelta(days=182)
