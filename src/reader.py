import json

class Reader:
    def __init__(self):
        """Load the json file."""
    def load_file(spell_search):
        for file in os.listdir("spells"):
            if file == f"{spell_search}.json":
                with open(f"spells/{spell_search}.json", 'r') as file:
                    spell_read = json.load(file)
