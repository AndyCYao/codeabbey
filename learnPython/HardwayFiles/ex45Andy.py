''' I am going to write a short game, to practice
my oop. it will be a easy format of ex43.

User will start off in the main scene, call
hallway

there will be three more scenes after this hall way
so in total there will be for:

for Scenes:
    Hallway
    Bathroom
    Bedroom
    End

for Engine: the main looper


for Map:
    map has a dictionary object that shows
    what scene to produce next.
'''
####################


class Scene(object):
    pass


class Hallway(Scene):

    def play(self):

        print("You are now in the Hallway - ",
              " a cold dark corridor with two doors")
        print("do you want to enter 1. Bathroom")
        print("2. Bedroom, or 3. Done?")
        x = int(input("enter a number > "))
        if x == 1:
            return "Bath_room"
        elif x == 2:
            return "Bed_room"
        elif x == 3:
            return "End"


class Bathroom(Scene):

    def play(self):

        print("You are now in the bathroom, smells nice")
        print("do you want to enter 1. Hallway")
        print("2. Bedroom, or 3. Done?")
        x = int(input("enter a number > "))
        if x == 1:
            return "Hall_way"
        elif x == 2:
            return "Bed_room"
        elif x == 3:
            return "End"


class Bedroom(Scene):

    def play(self):

        print("You are now in the bedroom, there's three beds",
              " one for papa, one for mama, and one for goldilock")
        print("do you want to enter 1. Hallway")
        print("2. Bedroom, or 3. Done?")
        x = int(input("enter a number > "))
        if x == 1:
            return "Hall_way"
        elif x == 2:
            return "Bed_room"
        elif x == 3:
            return "End"


class End(Scene):

    def play(self):
        print("Huzzah, you finished!")
        return "End"

#####################


class Engine(object):
    def __init__(self, starting):
        self.e_starting = starting  # passing a map object in here
        print("the engine got initliazed.")

    def play(self):
        print("Engine - Play")
        current_map = self.e_starting.start_map()
        last_map = self.e_starting.find_next_map("End")
        while current_map != last_map:
            next_map_string = current_map.play()
            current_map = self.e_starting.find_next_map(next_map_string)

            if current_map == last_map:
                current_map.play()


class Map(object):
    dict = {
        "Hall_way": Hallway(),
        "Bed_room": Bedroom(),
        "Bath_room": Bathroom(),
        "End": End()
    }

    def __init__(self, txtmap):
        self.start_scene = txtmap  # self._start_scene is an instance attribute of the the class,

    def find_next_map(self, txtmap):
        a = Map.dict.get(txtmap)
        print("In Map class, current returned map is: %s " % (a))
        return a

    def start_map(self):
        # assuming starting is always in Hallway
        b = self.find_next_map(self.start_scene)
        return b


a_map = Map("Hall_way")
a_game = Engine(a_map)
a_game.play()
