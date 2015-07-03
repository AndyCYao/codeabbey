class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        print("Game started, welcome")


class Death(Scene):

    def enter(self):
        print("sorry, you died, thank you come again")


class CentralCorridor(Scene):

    def enter(self):
        print("You are now in Central Corridor")


class LaserWeaponArmory(Scene):

    def enter(self):
        print("You are now in the Laser Weapon Armory")


class TheBridge(Scene):

    def enter(self):
        print("You are now in the Bridge")


class EscapePod(Scene):

    def enter(self):
        print("You are now in the escape")


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

# a_map = Map('central_corridor')
# a_game = Engine(a_map)
# a_game.play()
