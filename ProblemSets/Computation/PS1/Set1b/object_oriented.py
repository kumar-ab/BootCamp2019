class Backpack:
    '''
    A Backpack object class. Has a name, color, maximum size and a list of contents.
    Attributes:
    name (str): the name of the backpack's owner.
    name (str): the name of the backpack's owner.
    color (str): color of the backpack
    max_size (int): maximum items that can be put in the backpack
    contents (list): the contents of the backpack.
    '''
    def __init__(self, name, color, max_size=5): # This function is the constructor.
        '''
        Parameters:
        name (str): the name of the backpack's owner.
        color (str): color of the backpack
        max_size (int): maximum items that can be put in the backpack
        '''
        self.name = name # Initialize some attributes.
        self.color = color
        self.max_size = max_size
        self.contents = []

    def put(self, item):
        '''
        method to put an item into the backpack
        Items can only be put if the contents don't reach the max_size
        '''
        item_count = len(self.contents)
        if item_count < self.max_size:
            self.contents.append(item)
        else:
            print("No room!")

    def take(self, item):
        '''
        method to take items from the Backpack
        if the item is not present it cannot be taken
        '''
        item_count = len(self.contents)
        if (item in self.contents):
            self.contents.remove(item)
        else:
            print(f"{item} not there!")

    def dump(self):
        '''
        method to remove all items from the backpack
        '''
        self.contents.clear()


class Jetpack(Backpack):
    '''
    A Jetpack object inheriting from the Backpack class.
    Has a name, color, maximum size, fuel and a list of contents.
    Attributes:
    name (str): the name of the backpack's owner.
    name (str): the name of the backpack's owner.
    color (str): color of the backpack
    max_size (int): maximum items that can be put in the backpack
    fuel (int): amount of fuel in the backpack
    contents (list): the contents of the backpack.
    '''
    def __init__(self, name, color, max_size=2, fuel=10): # This function is the constructor.
        '''
        Parameters:
        name (str): the name of the backpack's owner.
        color (str): color of the backpack
        max_size (int): maximum items that can be put in the backpack
        '''
        Backpack.__init__(self, name, color, max_size)
        self.fuel = fuel

    def fly(self, f_burn):
        '''
        method for flyinf
        Input = amount of fuel to comsume
        '''
        if f_burn > self.fuel:
            print("Not enough fuel!")
        else:
            self.fuel -= f_burn

    def dump(self):
        '''
        method to remove all items from the backpack and empty the fuel tank
        '''
        self.contents.clear()
        self.fuel = 0


class ContentFilter:
    '''
    A ContentFilter class.
    Attributes:
    filename (str): the filename to check.
    '''
    def __init__(self, fname): # This function is the constructor.
        self.filename = fname
        self.f_open()

    def f_open(self):
        try:
            myfile = open(self.filename)
        except FileNotFoundError:
            self.filename = input("Please enter a valid file name: ")
            self.f_open()
        except TypeError:
            self.filename = input("Please enter a valid file name: ")
            self.f_open()
        except TypeError:
            self.filename = input("Please enter a valid file name: ")
            self.f_open()
        else:
            myfile.close()
