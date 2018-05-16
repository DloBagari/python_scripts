class UnitValue_1:
    def __init__(self, unit):
        self.value = None
        self.unit = unit
        self.default_format = "5.2f"

    def __set__(self, instance, value):
        self.value = value

    def __str__(self):
        return " {value:{spec}} {unit}".format(spec = self.default_format,
                                               **self.__dict__)

    def format(self, spec="5.2f"):
        if spec =="":
            spec = self.default_format
        return " {value:{spec}} {unit}".format(spec = self.default_format,
                                               **self.__dict__)
        

class RTD_1:
    __rate = UnitValue_1("kt")
    time = UnitValue_1("hr")
    distance = UnitValue_1("nm")

    def __init__(self, rate=None, time=None, distance=None):
        if rate is None:
            self.time = time
            self.distance= diatance
            self.__rate = distance / time

        if time is None:
            self.__rate = rate
            self.distance = distance
            self.time = distance / rate

        if distance is None:
            self.__rate = rate
            self.time = time
            self.distance = tate * time

    def __str__(self):
        return" rate: {0}".format(self.__rate)
             
