class Unit:
    conversion = 1.0

    def __get__(self, instance, owner):
        return instance.kph * self.conversion

    def __set__(self, instance, value):
        instance.kph = value / self.conversion

class Knotes(Unit):
    conversion = 0.5399568


class MPH(Unit):
    conversion = 0.62137119


class KPH(Unit):

    def __get__(self, instance, owner):
        return instance._kph

    def __set__(self, instance, value):
        instance._kph = value
        instance._dlo = 3

class Measurement:
    kph = KPH()
    knotes = Knotes()
    mph = MPH()

    def __init__(self, kph=None, knotes=None, mph=None):
        if kph: self.kph = kph
        elif knotes: self.knotes = knotes
        elif mph: self.mph = mph
        else:
            raise TypeError

    def __str__(self):
        return " Rates: {0.kph} kph = {0.knotes} knotes = {0.mph} mph".format(self)
    
