import numbers
import math

class FixedPoint(numbers.Rational):
    __slots__ = ("value", "scale", "default_format")

    def __new__(cls, value, scale=100):
        self = super().__new__(cls)
        if isinstance(value, FixedPoint):
            self.value = value.value
            self.scale = value.scale
        elif isinstance(value, int):
            self.value = value
            self.scale = scale
        elif isinstance(value, float):
            self.value = int(value*scale+.5)
            self.scale = scale
        else:
            raise TypeError

        digits = int(math.log10(scale))
        self.default_format = "{{0:.{digits}f}".format(digits=digits)
        return self
    def __str__(self):
        return self.__format__(self.default_format)

    def __repr__(self):
        return "{__class__.__name__}({value:d}, scale = {scale:d})".format(\
            __class__ = self.__class, value = self.value, scale = self.scale)

    def __format__(self, spec):
        if spec == "":
            spec = self.default_format
        return spec.format(self.value/ self.scale)

    def numerator(self):
        return self.value

    def denominator(self):
        return self.scale

    def __abs__(self):
        pass
    
    
