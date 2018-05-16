from q import *

class Sc:

    def __init__(self, levels,timeSlice):
        self.__levels = Link()
        self.__buildLevels(levels,timeSlice)
        self.__counter = 0;

    def __buildLevels(self,levels, n):
        for i in range(levels):
            self.__levels.append(Level(i, n*2**i))
        for j in self.__levels:
            print(j.pr())


    def run(self,ready, block):
        try:
            while self.__counter != 0:
                for process in ready:
                    p = process.getPriorty()
                    self.__levels[p].append(p)
                    self.counter += 1
                
                    
                    
                    
        except IndexError:
           pass
