mystuff = {
	'apple': "I AM APPLES!"
}

print(mystuff['apple'])

import mystuff
mystuff.apple()
print(mystuff.tangerine)	

# Instead of importing module we can create a class
class MyStuff(object):

	def __init__(self):
		self.tangerine = "And now a thousand years between"

	def apple(self):
		print("I AM CLASSY APPLES!")

# Instantiate the class
thing = MyStuff()
thing.apple()
print(thing.tangerine)

# ways to get things from things

######### dict style
mystuff['apples']

######### module style
mystuff.apples()
print(mystuff.tangerine)

######### class style
thing = MyStuff()
thing.apple()
print(thing.tangerine)