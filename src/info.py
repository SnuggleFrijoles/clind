from request import Request
import json

class Info:
    url = "http://dnd5eapi.co/api/"
    topics = {
            "races": "http://dnd5eapi.co/api/races/",
            "subraces": "http://dnd5eapi.co/api/subraces/",
            "classes": "http://dnd5eapi.co/api/classes/",
            "subclasses": "http://dnd5eapi.co/api/subclasses/",
            "languages": "http://dnd5eapi.co/api/languages/",
            "spellcasting": "http://dnd5eapi.co/api/spellcasting/",
            "spells": "http://dnd5eapi.co/api/spells/",
            "monsters": "http://dnd5eapi.co/api/monsters/",
            "features": "http://dnd5eapi.co/api/features/",
            "tables": "http://dnd5eapi.co/api/tables/",
            "equipment": "http://dnd5eapi.co/api/equipment/",
            "proficiencies": "http://dnd5eapi.co/api/proficiencies/",
            "startingequipment": "http://dnd5eapi.co/api/startingequipment/"
            }


    def __init__(self, endpoint = url):
        self.endpoint = endpoint
        self.requester = Request()
        content = json.loads(str(self.requester.get(self.endpoint).decode('utf8')))
        self.count = content["count"]
        self.results = content["results"]

    def listResults(self):
        names = []
        for result in self.results:
            names.append(result["name"])

        return names

    @classmethod
    def listTopics(self):
        return topics.keys()


class Races(Info): 
    def __init__(self, endpoint):
        super().__init__("races/")
