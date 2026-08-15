class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught

    def speak(self):
        print(self.name)
        print(self.name)

    def display_details(self):
        print("Entry Number:", self.entry)
        print("Name:", self.name)
        print("Type:", self.types[0])
        print("Description:", self.description)
        if self.is_caught:
            print(self.name + " has already been caught!")
        else:
            print(self.name + " has not been caught yet!")


pikachu = Pokemon(25, "Pikachu", ["Electric"], "It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.", True)
charmander = Pokemon(4, "Charmander", ["Fire"], "It has a preference for hot things. When it rains, steam is said to spout from the tip of its tail.", False)
bulbasaur = Pokemon(1, "Bulbasaur", ["Grass", "Poison"], "For some time after its birth, it grows by using the nutrients that are stored in the seed on its back.", False)

pikachu.display_details()
pikachu.speak()

charmander.display_details()
bulbasaur.speak()