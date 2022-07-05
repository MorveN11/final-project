class Data:
    TOTAL_POPULATION = 0
    MORTALITY_RATE = 0
    INFECTED = 0

    @staticmethod
    def getTotalPopulation():
        return Data.TOTAL_POPULATION

    @staticmethod
    def setTotalPopulation(population):
        Data.TOTAL_POPULATION = population

    @staticmethod
    def getMortalityRate():
        return Data.MORTALITY_RATE

    @staticmethod
    def setMortalityRate(morality_rate):
        Data.MORTALITY_RATE = morality_rate

    @staticmethod
    def getInfected():
        return Data.INFECTED

    @staticmethod
    def setInfected(infected):
        Data.INFECTED = infected