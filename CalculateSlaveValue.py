class Slave:
    def __init__(self,
        age: int,
        opaque: int,
        strength: int,
        experience: int,
        environment: 'Environment',
        profession: 'Profession'
    ):
        self.age         = age
        self.opaque      = opaque
        self.strength    = strength
        self.experience  = experience
        self.environment = environment
        self.profession  = profession

    def getAge(self) -> int:
        return self.age

    def getOpaque(self) -> int:
        return self.opaque
    
    def setOpaque(self, opaque):
        self.opaque = opaque
    
    # Strength
    def getStrength(self) -> int:
        return self.strength
    
    def setStrength(self, strength):
        self.strength = strength

    def addStrength(self, strength):
        self.strength += strength 

    def subtractStrength(self, strength):
        self.strength -= strength

    # Experience
    def getExperience(self) -> int:
        return self.experience

    # Work Environment
    def getWorkEnvironment(self) -> 'Environment':
        return self.environment
    
    def setWorkEnvironment(self, environment):
        self.environment = environment
    
    # Profession
    def getProfession(self) -> 'Profession':
        return self.profession
    
    def setProfession(self, profession):
        self.profession = profession
    
class Environment:
    def __init__(self,
        temperature: int,
        difficulty: int
    ):
        self.temperature = temperature
        self.difficulty  = difficulty

    def getTemperature(self) -> int:
        return self.temperature
    
    def getDifficulty(self) -> int:
        return self.difficulty

class Profession:
    def __init__(self,
        name: str,
        demand: int,
        difficulty: int
    ):
        self.name       = name
        self.demand     = demand
        self.difficulty = difficulty

    def getName(self) -> str:
        return self.name
    
    def getDemand(self) -> int:
        return self.demand
    
    def getDifficulty(self) -> int:
        return self.difficulty

def calculateSlaveValue(slave):
    baseScore = 100
    baseScore += max(0, 100 - slave.getAge()) # Older the age, less the value
    baseScore += abs(slave.getOpaque() - slave.getWorkEnvironment().getTemperature()) # Calculate skin color advantage depending on the environment temperature
    baseScore += slave.getWorkEnvironment().getDifficulty() # If the environment is difficult to work in, better the value
    baseScore += slave.getProfession().getDemand() # If the demand for the job is higher, more value the slave is
    baseScore += slave.getProfession().getDifficulty() # If the job is difficult, better the value
    baseScore += slave.getStrength() # More strength the slave has, higher the value.
    baseScore += slave.getExperience() * 5 # More experience the slave has, higher the value.
    return baseScore

def calculateSlaveValueToMoney(slave):
    return calculateSlaveValue(slave) * 10

"""
Slave Information:

Age: 20
Skin Opaque: 50%
Strength Points: 46
Experience: 1 year
Environment: 40 Degrees Celcius, 50% Difficulty
Profession: Example1, 50% Demand, 20% difficulty
"""
exampleSlave = Slave(20, 50, 46, 1, Environment(40, 50), Profession("Example1", 50, 20))

print("Slave Value: $" + "{:,.2f}".format(calculateSlaveValueToMoney(exampleSlave)))

"""
Slave Information:

Age: 30
Skin Opaque: 100%
Strength Points: 50
Experience: 5 years
Environment: 50 Degrees Celcius, 40% Difficulty
Profession: Example2, 70% Demand, 60% difficulty
"""
exampleSlave = Slave(30, 40, 50, 5, Environment(50, 40), Profession("Example2", 70, 60))

print("Slave Value: $" + "{:,.2f}".format(calculateSlaveValueToMoney(exampleSlave)))