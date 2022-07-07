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

    @name.setter
    def name(self, newName):
        print('Setting Name')
        self.__name = newName

    @name.deleter
    def name(self):
        print('Deleting Name')
        del self.__name

    @property
    def species(self):
        print('Getting Species')
        return self.__species
    
    @property
    def habitat(self):
        print('Getting Habitat')
        return self.__habitat

    @habitat.setter
    def name(self, newHabitat):
        print('Setting Name')
        self.__habitat = newHabitat 

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

#-----------------------------------------------

class Fish(Animal):
    '''Fish Class, inheriting from Animal'''
    def __init__(self, name, species, habitat, color, weight, length):
        print('Initializing Fish')
        super().__init__(name)
        super().__init__(species)
        super().__init__(habitat)
        self.__color = color
        self.__weight = weight
        self.__length = length

    @property
    def color(self):
        print('Getting Color')
        return self.__color

    @color.setter
    def color(self, newColor):
        print('Setting Color')
        self.__color = newColor

    @property
    def weight(self):
        print('Getting Weight')
        return self.__weight

    @weight.setter
    def weight(self, newWeight):
        print('Setting Weight')
        self.__weight = newWeight
    
    @property
    def length(self):
        print('Getting Length')
        return self.__length

    @length.setter
    def length(self, newLength):
        print('Setting Length')
        self.__length = newLength 

    def swim(self):
        print(str(self.__name) + ' is swimming')

#-----------------------------------------------

class Snake(Animal):
    '''Snake Class, inheriting from Animal'''
    def __init__(self, name, species, habitat, color, length, venomous):
        print('Initializing Snake')
        super().__init__(name)
        super().__init__(species)
        super().__init__(habitat)
        self.__color = color
        self.__length = length
        self.__venomous = venomous

    @property
    def color(self):
        print('Getting Color')
        return self.__color

    @color.setter
    def color(self, newColor):
        print('Setting Color')
        self.__color = newColor

    @property
    def length(self):
        print('Getting Length')
        return self.__length

    @length.setter
    def length(self, newLength):
        print('Setting Length')
        self.__length = newLength 

    @property
    def venomous(self):
        print('Getting Venom Status')
        return self.__venomous

    @venomous.setter
    def weight(self, newVenomous):
        print('Setting Venom Status')
        self.__venomous = newVenomous

    def bite(self, bitee):
        print(str(self.__name) + ' bites' + str(bitee))

#-----------------------------------------------

class Person(Animal):
    '''Person Class, inheriting from Animal'''
    def __init__(self, name, species, habitat, height, weight, occupation):
        print('Initializing Person')
        super().__init__(name)
        super().__init__(species)
        super().__init__(habitat)
        self.__height = height
        self.__weight = weight
        self.__occupation = occupation

    @property
    def height(self):
        print('Getting Height')
        return self.__height

    @height.setter
    def height(self, newHeight):
        print('Setting Height')
        self.__height = newHeight
    
    @property
    def weight(self):
        print('Getting Weight')
        return self.__weight

    @weight.setter
    def weight(self, newWeight):
        print('Setting Weight')
        self.__weight = newWeight

    @property
    def occupation(self):
        print('Getting Occupation')
        return self.__occupation

    @occupation.setter
    def occupation(self, newOccupation):
        print('Setting Occupation')
        self.__occupation = newOccupation
    
    @occupation.deleter
    def occupation(self):
        print('Deleting Occupation')
        del self.__occupation

    def talk(self, listener, subject):
        print(str(self.__name) + ' is talking to ' + str(listener) + ' about ' + str(subject))

#-----------------------------------------------

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

    @name.setter
    def name(self, newName):
        print('Setting Name')
        self.__name = newName

    @name.deleter
    def name(self):
        print('Deleting Name')
        del self.__name

    @property
    def author(self):
        print('Getting Author')
        return self.__author

    @author.setter
    def author(self, newAuthor):
        print('Setting Author')
        self.__author = newAuthor
    
    @property
    def genre(self):
        print('Getting Genre')
        return self.__genre

    @genre.setter
    def genre(self, newGenre):
        print('Setting Genre')
        self.__genre = newGenre

    @genre.deleter
    def genre(self):
        print('Deleting Genre')
        del self.__genre

    def open(self):
        print('Opening ' + str(self.__name) + ' by ' + str(self.__author))

    def goTo_pg(pg):
        print('Going to page ' + str(pg))

    def close(self):
        print('Closing ' + str(self.__name) + ' by ' + str(self.__author))

#-----------------------------------------------

class Textbook(Book):
    '''Textbook Class, inheriting from Book'''
    def __init__(self, name, author, genre, subject, edition):
        print('Initializing Textbook')
        super().__init__(name)
        super().__init__(author)
        super().__init__(genre)
        self.__subject = subject
        self.__edition = edition

    @property
    def subject(self):
        print('Getting Subject')
        return self.__subject

    @subject.setter
    def subject(self, newSubject):
        print('Setting Subject')
        self.__subject = newSubject

    @subject.deleter
    def subject(self):
        print('Deleting Subject')
        del self.__subject
    
    @property
    def edition(self):
        print('Getting Edition')
        return self.__edition

    @edition.setter
    def edition(self, newEdition):
        print('Setting Edition')
        self.__edition = newEdition

    @edition.deleter
    def edition(self):
        print('Deleting Edition')
        del self.__edition

    def goTo_section(section):
        print('Going to ' + str(section) + ' section')

#-----------------------------------------------

class AddressBook(Book):
    '''AddressBook Class, inheriting from Book'''
    def __init__(self, name, author, genre, location, year):
        print('Initializing AddressBook')
        super().__init__(name)
        super().__init__(author)
        super().__init__(genre)
        self.__location = location
        self.__year = year

    @property
    def location(self):
        print('Getting Location')
        return self.__location

    @location.setter
    def location(self, newLocation):
        print('Setting Location')
        self.__location = newLocation

    @location.deleter
    def location(self):
        print('Deleting Location')
        del self.__location
    
    @property
    def year(self):
        print('Getting Year')
        return self.__year

    def findName(thingName):
        print(str(thingName) + '\'s Address')
        return thingName['Address']

#-----------------------------------------------

class Vehicle:
    '''Vehicle Class'''
    def __init__(self, name, _type, environment):
        print('Initializing Vehicle')
        self.__name = name
        self.__type = _type
        self.__environment = environment

    @property
    def name(self):
        print('Getting Name')
        return self.__name

    @name.setter
    def name(self, newName):
        print('Setting Name')
        self.__name = newName

    @name.deleter
    def name(self):
        print('Deleting Name')
        del self.__name

    @property
    def _type(self):
        print('Getting Type')
        return self.__type

    @property
    def environment(self):
        print('Getting Environment')
        return self.__environment

    def move(self):
        print(str(self.__name) + ' is moving')

#-----------------------------------------------

class Car(Vehicle):
    '''Car Class, inheriting from Vehicle'''
    def __init__(self, name, _type, environment, year, make, model, color):
        print('Initializing Car')
        super().__init__(name)
        super().__init__(_type)
        super().__init__(environment)
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

    @color.setter
    def color(self, newColor):
        print('Setting Color')
        self.__color = newColor

    def turnOn(self):
        print(str(self.__make) + ' ' + str(self.__model) + ' is on')

    def gas(self):
        print(str(self.__make) + ' ' + str(self.__model) + ' is driving')

    def _break(self):
        print(str(self.__make) + ' ' + str(self.__model) + ' is stopping')

    def turnOff(self):
        print(str(self.__make) + ' ' + str(self.__model) + ' is off')

#-----------------------------------------------

class Bicycle(Vehicle):
    '''Bicycle Class, inheriting from Vehicle'''
    def __init__(self, name, _type, environment, bikeType, gearType, color):
        print('Initializing Car')
        super().__init__(name)
        super().__init__(_type)
        super().__init__(environment)
        self.__bikeType = bikeType
        self.__gearType = gearType
        self.__color = color

    @property
    def bikeType(self):
        print('Getting Bicycle Type')
        return self.__bikeType

    @bikeType.setter
    def bikeType(self, newBikeType):
        print('Setting Bicycle Type')
        self.__bikeType = newBikeType

    @property
    def gearType(self):
        print('Getting Gear Type')
        return self.__gearType
    
    @gearType.setter
    def gearType(self, newGearType):
        print('Setting Gear Type')
        self.__gearType = newGearType

    @property
    def color(self):
        print('Gettering Color')
        return self.__color

    @color.setter
    def color(self, newColor):
        print('Setting Color')
        self.__color = newColor

    def pedal(rider):
        print(str(rider) + ' is pedaling')

    def turn(rider, direction):
        print(str(rider) + ' is turning ' + str(direction))

    def _break(rider):
        print(str(rider) + ' is stopping')

#-----------------------------------------------

class Boat(Vehicle):
    '''Boat Class, inheriting from Vehicle'''
    def __init__(self, name, _type, environment, size, boatType):
        print('Initializing Car')
        super().__init__(name)
        super().__init__(_type)
        super().__init__(environment)
        self.__size = size
        self.__boatType = boatType

    @property
    def size(self):
        print('Getting Size')
        return self.__size

    @size.setter
    def size(self, newSize):
        print('Setting Size')
        self.__size = newSize

    @property
    def boatType(self):
        print('Getting Boat Type')
        return self.__boatType
    
    @boatType.setter
    def boatType(self, newBoatType):
        print('Setting Boat Type')
        self.__boatType = newBoatType

    def dock(self, captian):
        print(str(captian) + ' is docking ' + str(self.__name))

    def steer(self, captian):
        print(str(captian) + ' is stearing ' + str(self.__name))

    def undock(self, captian):
        print(str(captian) + ' is undocking ' + str(self.__name))

#-----------------------------------------------

class HotAirBalloon(Vehicle):
    '''Hot-Air Balloon Class, inheriting from Vehicle'''
    def __init__(self, name, _type, environment, size, color):
        print('Initializing Car')
        super().__init__(name)
        super().__init__(_type)
        super().__init__(environment)
        self.__size = size
        self.__color = color

    @property
    def size(self):
        print('Getting Size')
        return self.__size

    @size.setter
    def size(self, newSize):
        print('Setting Size')
        self.__size = newSize

    @property
    def color(self):
        print('Gettering Color')
        return self.__color

    @color.setter
    def color(self, newColor):
        print('Setting Color')
        self.__color = newColor

    def takeOff(self):
        print(str(self.__name) + ' is taking off')

    def gas(self, pilot):
        print(str(pilot) + ' is heating ' + str(self.__name))

    def land(self, pilot):
        print(str(pilot) + ' is landing ' + str(self.__name))