class Circle:
    '''
    Description of Circle

    This class deals with circles

    Class attributes:
        all_circles: list of all circles
        pi: number of PI

    Attributes:
         rad: radius

    Methods:
          area: shows square

    Static methods:
        total_area: shows square of all circles
    '''
    all_circles = []
    pi = 3.1415

    def __init__(self, rad=1):
        '''
        Initializes circle

        Args:
            rad: radius
        '''
        self.rad = rad
        self.all_circles.append(rad)

    def area(self):
        '''
        Method shows square

        returns number of square
        '''
        S = Circle.pi * self.rad ** 2
        return S

    @staticmethod
    def total_area():
        '''
        Method countes number of all squares

        returns number of all squares
        '''
        sum_S = 0
        for itr in Circle.all_circles:
            sum_S += itr ** 2 * Circle.pi

        return sum_S

    def __repr__(self):
        '''
        method of printing

        return string with radius
        '''
        return str(self.rad)