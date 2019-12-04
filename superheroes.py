import random

class Ability:
    def __init__(self, name, attack_strength):
        '''
       Initialize the values passed into this
       method as instance variables.
        '''

        # Assign the "name" and "max_damage"
        # for a specific instance of the Ability class
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
      ''' Return a value between 0 and the value set by self.max_damage.'''

      # Pick a random value between 0 and self.max_damage
      random_value = random.randint(0,self.attack_strength)
      return random_value


class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        # TODO: Create instance variables for the values passed in.
        self.name = name
        self.max_block = max_block
        pass

    def block(self):
        '''
        Return a random value between 0 and the
        initialized max_block strength.
        '''

        random_value = random.randint(0, self.max_block)
        return random_value
        pass


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    armor = Armor("Debugging Shield", 10)
    print(armor.name)
    print(armor.block())
