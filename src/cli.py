
import random

from roller import Roller
from exceptions import *

class CLI():
    """
    class: CLI

    Defines the command line interface.
    """

    def __init__(self):
        """
        Constructor
        """
        
        pass

    def askForCommand(self):
        """
        Method: askForCommand

        Get a command from the user.
        """

        command = input("> ")

        return command

    
    def processCommand(self, whole_command):
        """
        Method: processCommand

        Interpret a command
        """
        
        command_split = whole_command.split(" ")

        command_word = command_split[0]

        if command_word == "roll":
            
            if len(command_split) == 2:
                
                roller_string = command_split[1]

                roller = Roller(roller_string)

                return roller.roll()

            else:

                raise ClindException("Error: roll requires exactly one argument")

        elif command_word == "exit":

            pass

        elif command_word == "name":

            with open("src/names.txt") as names_file:

                names = list(names_file)
            
                return random.choice(names).strip() + " " + random.choice(names).strip()

        else:

            raise ClindException("Error: command {} not recognized".format(command_word))


    
    def run(self):
        """
        Method: run

        Run the CLI until completion
        """

        command = ""

        while command != "exit":

            command = self.askForCommand()

            try:
                
                result = self.processCommand(command)
                
                if result != None:
                    
                    print(result)

            except ClindException as e:
                
                print(e.message)



