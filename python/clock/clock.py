import math

class Clock:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        self.result = self.prepare_clock()

    def __str__(self):
        return self.result

    def __eq__(self, other):
        return self.result == other.result

    def prepare_clock(self):
        self.sanitize_minutes()
        formatted_hour = "%02d" % (self.hours % 24)
        formatted_minutes = "%02d" % (self.minutes)
        self.result = '%s:%s' %(formatted_hour, formatted_minutes)
        return self.result

    def sanitize_minutes(self):
        if 0 <= self.minutes < 60:
            return self.minutes
        elif self.minutes >= 60:
            self.hours = self.hours + 1
            self.minutes = self.minutes - 60
            self.sanitize_minutes()
        elif self.minutes <= -60:
            self.hours = self.hours - 1
            self.minutes = self.minutes + 60
            self.sanitize_minutes()
        else:
            self.hours = self.hours - 1
            self.minutes = 60 + self.minutes

    def add(self, minutes):
        self.minutes = self.minutes + minutes
        return self.prepare_clock()
