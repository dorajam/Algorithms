# Dora Jambor, dorajambor@gmail.com
# January, 2016
# MIT 6.00.1x Introduction to Computer Science and Programming Using Python

# Practice for understanding __eq__ and __repr__ methods.

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
        
    def __eq__(self, other):
        # Check other to be of the same type
        assert type(other) == type(self)
        # Then check if coordinates are the same
        return self.getX() == other.getX() and self.getY() == other.getY()
        
    def __repr__(self):
        return 'Coordinate(%i, %i)'%(self.x,self.y)
