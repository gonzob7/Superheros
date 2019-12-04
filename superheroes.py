import random
from random import choice

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

        self.isWinner = False



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

    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths'''
        # TODO: This method should add the number of deaths to self.deaths
        self.deaths += num_deaths
        pass

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
            self.isWinner = True
            self.add_kill(1)
            opponent.add_death(1)
        elif opponent.is_alive() and not self.is_alive():
            opponent.add_kill(1)
            self.add_death(1)
            opponent.isWinner = True
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

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print("{} Kill/Deaths:{}".format(hero.name,kd))

    def revive_heroes(self):
        ''' Reset all heroes health to starting_health'''
        # TODO: for each hero in self.heroes,
        # set the hero's current_health to their starting_health
        for hero in self.heroes:
            hero.current_health = hero.starting_health
        pass

    def attack(self, other_team):
        ''' Battle each team against each other.'''

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents)> 0:
            # TODO: Complete the following steps:
            # 1) Randomly select a living hero from each team (hint: look up what random.choice does)
            hero1 = choice(self.heroes)
            hero2 = choice(other_team.heroes)
            # 2) have the heroes fight each other (Hint: Use the fight method in the Hero class.)
            hero1.fight(hero2)
            # 3) update the list of living_heroes and living_opponents
            # to reflect the result of the fight
            if hero1.isWinner == True:
                living_opponents.remove(hero2)
            elif hero2.isWinner == True:
                living_heroes.remove(hero1)
            else:
                living_heroes.remove(hero1)
                living_opponents.remove(hero2)

class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        # TODO: create instance variables named team_one and team_two that
        # will hold our teams.
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        name = input("What is the ability name?: ")
        max_damage = input("What is the max damage of the ability?: ")

        return Ability(name, max_damage)

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        # TODO: This method will allow a user to create a weapon.
        # Prompt the user for the necessary information to create a new weapon object.
        # return the new weapon object.
        name = input("What is the weapon name?: ")
        max_damage = input("What is the max damage of this weapon?: ")
        return Weapon(name, max_damage)
        pass

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        # TODO:This method will allow a user to create a piece of armor.
        #  Prompt the user for the necessary information to create a new armor object.
        #  return the new armor object with values set by user.
        name = input("What is the armor name?: ")
        max_block = input("What is the max block of this armor?: ")
        return Armor(name, max_block)
        pass

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
           add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
           if add_item == "1":
               #TODO add an ability to the hero
               create_ability()
           elif add_item == "2":
               #TODO add a weapon to the hero
               create_weapon()
           elif add_item == "3":
               #TODO add an armor to the hero
               create_armor()
        return hero

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        # TODO: This method should allow a user to create team one.
        # 1) Prompt the user for the name of the team
        team_name = input("What is the name for team 1?: ")
        # 2) Prompt the user for the number of Heroes on the team
        num_heroes = int(input("How many heroes on this team?: "))
        # 3) Instantiate a new Team object,
        # using the team name obtained from user input
        team_one = Team(team_name)
        # 4) use a loop to call self.create_hero() for the number
        # of heroes the user specified the team should have,
        # and then add the heroes to the team.
        for i in range(0, num_heroes):
            hero = self.create_hero()
            team_one.add_hero(hero)
        pass

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        # TODO: This method should allow a user to create team one.
        # 1) Prompt the user for the name of the team
        team_name = input("What is the name for team 1?: ")
        # 2) Prompt the user for the number of Heroes on the team
        num_heroes = int(input("How many heroes on this team?: "))
        # 3) Instantiate a new Team object,
        # using the team name obtained from user input
        team_two = Team(team_name)
        # 4) use a loop to call self.create_hero() for the number
        # of heroes the user specified the team should have,
        # and then add the heroes to the team.
        for i in range(0, num_heroes):
            hero = self.create_hero()
            team_two.add_hero(hero)
        pass

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
        team_one.attack(team_two)
        pass

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
