#Python control flow using match statement

'''
match case only works on python3.10 and higher version only
structural pattern matching has beeb added in the form of match statements and case statenments of the patterns associaated with actions.
patterns consists of :
                sqeuences,
                mappings,
                premitive data types,
                class instances

Pattern matching enables extracting information from complex data types, apply specific actions based different forms of data

A match satetement takes an expression and compares it value to sucessive patterns given as one or case blocks
'''

#basic Intro with example

def http_error(status):
    match status:
        case 400:
            return 'Bad rewuest'
        case 404:
            return 'Not found'
        case 418:
            return "I'm a teapot"
        case _:
            return "Something is wrong with the internet"

def http_error(status):
    match status:
        case 400 | 404 | 403:
            return 'not allowed'
        case 418:
            return "I'm a teapot"
        case _:
            "Something's wrong with the internet"
#Testing the method
http_error(400)

#Patherns can look like unpacking assignments, and can be used to bind variables
#point is as an (x,y,z) tuple

def coordinates(point):
    match point:
        case 0:
            print('Origin')
        case (0,y,0):
            print(f"Y: {y}")
        case (x,0,0):
            print(f"X: {x}")
        case (0,0,z):
            print(f"Z: {z}")
        case (x,y):
            print(f"X: {x}, Y:{y}")
        case (x,z):
            print(f"X: {x}, Y:{z}")
        case (y,z):
            print(f"Y: {y}, Z:{z}")
        case (x,y,z):
            print(f"X: {x} Y: {y}, Z:{z}")
        case _:
            raise ValueError('Not a point')
#Testing the function with a point tuple
point_tuple = (0,0)
point_tuple1 = (0,123)
point_tuple2 = (123,0)
point_tuple3 = (123,456)
coordinates(point_tuple)

# Using match- case with class
from dataclasses import dataclass
@dataclass
class Point:
    x: int
    y: int
    z: int
def where_is(point):
    match point:
        case Point(x=0,y=0):
            print('Origin')
        case Point(x= 0, y = y):
            print(f"Y={y}")
        case Point(x= x, y = 0):
            print(f"X={x}")
        case Point():
            print("Not on the orgin")
        case _:
            print("Not allowed")

where_is(Point(0,0))
where_is(Point(0,10))
where_is(Point(10,0))
where_is(Point(10,10))

#Smart alarm for work-life balance---- it displays some message to appreciate the user for completing some task or what to do during the day

#
def alarm(item):
    match item:
        case ['evening',action]:
            print(f'You almost finished your day!. Now {action}')
        case [time,'action']:
            print(f"Good {time}! It is time to {action}!")
        case _:
            print('Invalid time and action')

alarm(['evening','play video games'])
alarm(['evening','work'])

#making it more smarter
def smart_alarm(item):
    match item:
        case ['evening',action] if action not in ['work','study']:
            print(f"You almost finished the day! Now {action}!")
        case ['evening',_]:
            print(f"Come on! You should take some rest!")
        case [time,action]:
            print(f"Good {time}! It is time to {action}!")
        case _:
            print('Invalid time')

smart_alarm(['evening','study'])


#match -case used in a class instance to match a class object

class Direction:
#pass
    def __init__(self, horizontal= None, vertical=None):
        self.horizontal = horizontal
        self.vertical = vertical
# we can use  a match- case synthax to match an instance from this class display a message based on the attributes
def direction(loc):
    match loc:
        case Direction(horizontal = 'East', vertical='North'):
            print(f'You are heading towards North-East')
        case Direction(horizontal='east', vertical='south'):
            print('You towards southeast')
        case Direction(horizontal='west', vertical='north'):
            print('You towards northwest')
        case Direction(horizontal='west', vertical='south'):
            print('You towards southwest')
        case Direction(horizontal=None):
            print(f'You towards {loc.vertical}')
        case Direction(vertical=None):
            print(f'You towards {loc.horizontal}')
        case _:
            print('Invalid Direction')

#lets create some on=bjects from the class for testing

d1 = Direction('East','North')
d2 = Direction(vertical=None)
d3 = Direction('center','center')

direction(d1)
direction(d2)
direction(d3)
