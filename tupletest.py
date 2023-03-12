#to use namedtuples the library has to be imported
from collections import namedtuple

#Player named tuple | Player = namedtuple(defined variables)
#Player is requred, it's what we are defining
Player = namedtuple('Player', ['name', 'number', 'position', 'team'])

#names for tuple and their values
cam = Player('Cam Newton', '1', 'Quarterback', 'Carolina Panthers')
lebron = Player('Lebron James', '23', 'Small forward', 'Los Angeles Lakers')

#prints of what the data with calls based on their tuples
print(cam.name + '(#' + cam.number + ')' + ' is a ' + cam.position + ' for the ' + cam.team + '.')
print(lebron.name + '(#' + lebron.number + ')' + ' is a ' + lebron.position + ' for the ' + lebron.team + '.')

#section 3.3 for more info
#tuple can be a list of data that can be called via assigning variables
#