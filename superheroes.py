import random

class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        # abilities and armors don't have starting values,
        # and are set to empty lists on initialization
        self.abilities = list()
        self.armors = list()
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health

        self.deaths = 0
        self.kills = 0



    def add_ability(self, ability):
        ''' Add ability to abilities list '''

        # We used the append method to add strings to a list
        # in the Rainbow Checklist tutorial. This time,
        # we're not adding strings, instead we'll add ability objects.
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # TODO: This method will append the weapon object passed in as an
        # argument to self.abilities.
        # This means that self.abilities will be a list of
        # abilities and weapons.
        self.abilities.append(weapon)
        pass

    def attack(self):
      # start our total out at 0
        total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
        # return the total damage
        return total_damage

    def add_armor(self, armor):
      # TODO: Add armor object that is passed in to `self.armors`
      self.armors.append(armor)



    def defend(self):
      '''Calculate the total block amount from all armor blocks.
         return: total_block:Int
      '''
      # TODO: This method should run the block method on each armor in self.armors
      total_block = 0
      for armor in self.armors:
          total_block = total_block + armor.block()
      return total_block

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True
        pass
        
    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount'''
        self.kills += num_kills

    def take_damage(self, damage):

      # TODO: Create a method that updates self.current_health to the current
      # minus the the amount returned from calling self.defend(damage).
        defense = self.defend()
        self.current_health -= damage - defense


    def fight(self, opponent):
      # TODO: Fight each hero until a victor emerges.
      # Phases to implement:
      # 0) check if at least one hero has abilities. If no hero has abilities, print "Draw"
        while self.is_alive() and opponent.is_alive():
            self.take_damage(opponent.attack())
            opponent.take_damage(self.attack())
        if self.is_alive() and not opponent.is_alive():
            print(self.name, 'won!')
        elif opponent.is_alive() and not self.is_alive():
            print(opponent.name, 'won!')
        else:
            print('Draw!')
      # 1) else, start the fighting loop until a hero has won
      # 2) the hero (self) and their opponent must attack each other and each must take damage from the other's attack
      # 3) After each attack, check if either the hero (self) or the opponent is alive
      # 4) if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop
        pass


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

class Weapon(Ability):
    def attack(self):

        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        # TODO: Use integer division to find half of the max_damage value
        # then return a random integer between half of max_damage and max_damage
        random_value = random.randint((self.attack_strength//2),self.attack_strength)
        return random_value
        pass

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        foundHero = False
        # loop through each hero in our list
        for hero in self.heroes:
            # if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
                # set our indicator to True
                foundHero = True
        # if we looped through our list and did not find our hero,
        # the indicator would have never changed, so return 0
        if not foundHero:
            return 0

    def view_all_heroes(self):
            '''Prints out all heroes to the console.'''
            # TODO: Loop over the list of heroes and print their names to the terminal one by one.
            for hero in self.heroes:
                print(hero.name)
            pass

    def add_hero(self, hero):
      '''Add Hero object to self.heroes.'''
      # TODO: Add the Hero object that is passed in to the list of heroes in
      # self.heroes
      self.heroes.append(hero)
      pass

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
