class Animal:
    '''Animal Class'''
    def __init__(self, name, species, habitat):
        print('Initializing Animal')
        self.__name = name
        self.__species = species
        self.__habitat = habitat

    @property
    def name(self):
        print('Getting Name')
        return self.__name

    @property
    def species(self):
        print('Getting Species')
        return self.__species
    
    @property
    def habitat(self):
        print('Getting Habitat')
        return self.__habitat

    @name.setter
    def name(self, newName):
        print('Setting Name')
        self.__name = newName

    @species.setter
    def name(self, newSpecies):
        print('Setting Species')
        self.__species = newSpecies

    @habitat.setter
    def name(self, newHabitat):
        print('Setting Name')
        self.__habitat = newHabitat 

    @name.deleter
    def name(self):
        print('Deleting Name')
        del self.__name

    @species.deleter
    def species(self):
        print('Deleting Species')
        del self.__species

    @habitat.deleter
    def habitat(self):
        print('Deleting Habitat')
        del self.__habitat

    def move(self):
        print(str(self.__name) + ' is moving')

    def sleep(self):
        print(str(self.__name) + ' is sleeping')

    def eat(self):
        print(str(self.__name) + ' is eating')

#---------------------------------------

class Book:
    '''Book Class'''
    def __init__(self, name, author, genre):
        print('Initializing Book')
        self.__name = name
        self.__author = author
        self.__genre = genre

    @property
    def name(self):
        print('Getting Name')
        return self.__name

    @property
    def author(self):
        print('Getting Author')
        return self.__author
    
    @property
    def genre(self):
        print('Getting Genre')
        return self.__genre

    @name.setter
    def name(self, newName):
        print('Setting Name')
        self.__name = newName

    @author.setter
    def author(self, newAuthor):
        print('Setting author')
        self.__author = newAuthor

    @genre.setter
    def genre(self, newGenre):
        print('Setting Genre')
        self.__genre = newGenre

    @name.deleter
    def name(self):
        print('Deleting Name')
        del self.__name

    @author.deleter
    def author(self):
        print('Deleting Author')
        del self.__author

    @genre.deleter
    def genre(self):
        print('Deleting Genre')
        del self.__genre

    def open(self):
        print('Opening ' + str(self.__name) + ' by ' + str(self.__author))

    def goTo_pg(self, pg):
        print('Going to page ' + str(pg))

    def close(self):
        print('Closing ' + str(self.__name) + ' by ' + str(self.__author))


class Vehicle:
    '''Vehicle Class'''
    def __init__(self, year, make, model, color):
        print('Initializing Animal')
        self.__year = year
        self.__make = make
        self.__model = model
        self.__color = color

    @property
    def year(self):
        print('Getting Year')
        return self.__year

    @property
    def make(self):
        print('Getting Make')
        return self.__make
    
    @property
    def model(self):
        print('Getting Model')
        return self.__model

    @property
    def color(self):
        print('Gettering Color')
        return self.__color

    @year.setter
    def year(self, newYear):
        print('Setting Year')
        self.__year = newYear

    @make.setter
    def make(self, newMake):
        print('Setting Make')
        self.__make = newMake

    @model.setter
    def model(self, newModel):
        print('Setting Model')
        self.__model = newModel

    @color.setter
    def color(self, newColor):
        print('Setting Color')
        self.__color = newColor

    @color.deleter
    def color(self):
        print('Deleting Color')
        del self.__color


    def turnOn(self):
        print(str(self.__make) + ' ' + str(self.__model) + ' is on')

    def gas(self):
        print(str(self.__make) + ' ' + str(self.__model) + ' is driving')

    def _break(self):
        print(str(self.__make) + ' ' + str(self.__model) + ' is stopping')

    def turnOff(self):
        print(str(self.__make) + ' ' + str(self.__model) + ' is off')