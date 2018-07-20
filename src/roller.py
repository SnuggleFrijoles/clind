import random 

class Roller():
    """
    class: Roller

    Execute a roll based on a roll string like 2d20+3
    """

    def __init__(self, die_string):

        self.die_string = die_string
        
        if "d" in self.die_string:

            split = self.die_string.split("d")
            
            
            if split[0] == '':
                self.n = 1
            else:
                self.n = int(split[0])

            rest = split[1]


            if "+" in rest:
                
                split = rest.split("+")

                self.die = int(split[0])
                self.plus = int(split[1])

            else:

                self.die = int(rest)
                self.plus = 0

        elif "+" in self.die_string:
            
            split = self.die_string.split("+")

            self.die = int(split[0])
            self.plus = int(split[1])
            self.n = 1

        else:

            self.die = int(self.die_string)
            self.plus = 0
            self.n = 1
    

    def roll(self):

        total = 0
        
        for i in range(self.n):

            total += random.randint(1, self.die)

        total += self.plus

        return total


