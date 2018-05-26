from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
	
	def enter(self):
		print("This scene is not yet configured.")
		print("Subclass it and implement enter().")
		exit(1)

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')

		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

		# be sure to print out the last scene
		current_scene.enter()

class Death(Scene):

	quips = [
	"You died. You kinda suck at this.",
	"Your Mom would be proud...if you were smarter.",
	"LOOOOSSSSSEEEEERRRRR",
	"I have a small puppy that is better at this.",
	"You're worse than your Dad's jokes."
	]

	def enter(self):
		print(Death.quips[randint(0, len(self.quips) - 1)])
		exit(1)

class CentralCorridor(Scene):

	def enter(self):
		print(dedent("""
			The Gothons of Planet Percal #25 have invade your ship and
			destroyed your entire crew! OH NO! You are the only survivor
			and your last mission is to get to the neutron bomb from the
			Weapons Armory, put it in the bridge, and blow the ship up
			after getting into an escape.

			You're running down the central corridor to the Weapons Armory
			when a Gothon jumps out, red scaly skin, dark grimy teeth, and
			evil clown costume flowing around his hate-filled body. He's
			blocking the door to the Armory and about to pull a weapon to blast you.
			"""))

		action = input(">>> ")

		if action == "shoot!":
			print(dedent("""
				You yank out your blaster and fire!  His clown costume is flowing and
				moving around his body, throwing off your aim.  Your laser hits his
				costume but misses his body.  This ruins his brand new costume that his
				mother bought him, making him fly into an insane rage and blast you
				in the face until you are dead. Then he eats.
				"""))
			return 'death'

		elif action == "dodge!":
			print(dedent("""
				Like a world class boxer you dodge, weave, slip and slide right as the
				Gothon's blaster cranks a laser past your head. In the middle of your
				artful dodge your foot slips and you bang your head on the metal wall
				and pass out. The Gothom stomps on your head and eats you.
				"""))
			return 'death'

		elif action == 'tell a joke':
			print(dedent("""
				Lucky for you they made you learn Gothon jokes in the academy. You tell
				the Gothon the one joke you know: Lfds eokur jura fur wehoon, elvo rupnum
				bernol kuchinka wir. The Gothon stops, tries not to laugh, then bursts out
				laughing and can't move. You shoot him in the head putting him down, then 
				jump through the Weapon Armory door.
				"""))
			return 'laser_weapon_armory'

		else:
			print("DOES NOT COMPUTER!")
			return 'central_corridor'

class LaserWeaponArmory(Scene):

	def enter(self):
		print(dedent("""
			You dive roll into the Armory and scan the room.  It's dead quiet, too quiet...
			You stand up and run to the neutron bomb, it is in a locked container and you 
			need a code to open it.  If you get the code wrong 10 times the bomb locks forever
			and you can't get to it.  The code is 3 digits.
			"""))

		code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
		guess = input("[keypad]>>> ")
		guesses = 0

		while guess != code and guesses < 10:
			print('BZZZZZZEDD!')
			guesses += 1
			guess = input("[keypad]>>> ")

		if guess == code:
			print(dedent("""
				The container clicks open!  You grab the bomb and run as fast as you can
				to the bridge, where you must place it in the right spot.
				"""))
			return 'the_bridge'
		else: 
			print(dedent("""
				The lock buzzes and you hear an audible click and flash, as the seal of the
				container melts itself permanently into place, you decide to sit there and
				wait for sweet death, which comes when a Gorthon shoots you and eats your legs.
				"""))
			return 'death'

class TheBridge(Scene):

	def enter(self):
		print(dedent("""
			You burst into the bridge, bomb in hand! Five Gorthon's are already in the room
			trying to take control of the ship. Each of them has an uglier clown costume than the
			last.  They haven't pulled their weapons out yet, as they see the bomb in your arm
			and don't want to set it off.
			"""))

		action = input(">>> ")

		if action == 'throw the bomb':
			print("You panic and throw the bomb, the Gothon's fire and the bomb explodes killing you.")
			return 'death'

		elif action == "slowly place the bomb":
			print(dedent("""
				You point your blaster at the bomb under your arm and the Gothon's drop their weapons.
				You inch towards the door, place the bomb, blow the door control panel and run away locking
				the Gothon's in.  Now you need to get to the escape pod!
				"""))
			return 'escape_pod'

		else:
			print("DOES NOT COMPUTE")
			return "the_bridge"

class EscapePod(Scene):

	def enter(self):
		print(dedent("""
			You rush deparately through the ship trying to make it to the escape pods before the ship
			explodes.  You're lucky enough to not run into any Gothons along the way.  When you finally
			make it to the pod room you find three pods remaining, though some may be damaged you can't tell
			which.  There are 3 pods, which one do you take?
			"""))

		good_pod = randint(1,5)
		guess = input("[pod #]>>> ")

		if int(guess) != good_pod:
			print(dedent("""
				You jump into pod {guess} and hit the eject button.  The last thing you hear is a click and boom
				as the hull ruptures and you get sucked out into the void of space.
				"""))
			return 'death'

		else:
			print(dedent("""
				You jump into pod {guess} and hit the eject button.  The pod slides out into space
				heading to the planet.  The ship explodes behind you taking the Gothon's ship with it.
				You won!!!
				"""))
			return 'finished'

class Finished(Scene):

	def enter(self):
		print("You won! Good job.")
		exit(1)

class Map(object):

	scenes = {
	'central_corridor': CentralCorridor(),
	'laser_weapon_armory': LaserWeaponArmory(),
	'the_bridge': TheBridge(),
	'escape_pod': EscapePod(),
	'death': Death(),
	'finished': Finished()
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()