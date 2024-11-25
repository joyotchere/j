#!/usr/bin/env python3
# Student ID: Joy Otchere
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(time1, time2):
    '''Returns the sum of two time objects'''
    total_seconds = time_to_sec(time1) + time_to_sec(time2)
    return sec_to_time(total_seconds)


def valid_time(t):
    """Check for the validity of the time object attributes:
       0 <= hour < 24, 0 <= minute < 60, 0 <= second < 60
    """
    return 0 <= t.hour < 24 and 0 <= t.minute < 60 and 0 <= t.second < 60

def change_time(time, seconds):
    '''Changes the time object by adding a specified number of seconds'''
    total_seconds = time_to_sec(time) + seconds
    return sec_to_time(total_seconds)

def time_to_sec(time):
    """Convert a time object to a single integer representing the number of seconds from midnight."""
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):
    """Convert a given number of seconds to a time object in hour, minute, second format."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

