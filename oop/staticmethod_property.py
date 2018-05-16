import math
class Angle(float):
    __slots__ = ("__degrees")

    @staticmethod
    def from_radian(value):
        return Angle(180 * value / math.pi)

    def __new__(cls, value):
        self = super().__new__(cls)
        self.__degrees = value
        return self

    @property
    def radian(self):
        return self.__degrees * math.pi /180

    @property
    def degrees(self):
        return self.__degrees
    
