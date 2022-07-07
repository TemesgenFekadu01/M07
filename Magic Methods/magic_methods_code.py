# Part 1
# ------------------------------

# Astronaut
# -----------------
# + name: string
# + status: string
# + flight: integer

# Part 2
# ------------------------------

import csv
import random

class Astronaut:
    '''Astronaut Class'''
    def __init__(self, name, status, flight):
        self.__name = name
        self.__status = status
        self.__flight = flight

    def __str__(self):
        return self.__name + ', ' + self.__status

    def __gt__(self, other):
        print('__gt__ called - self: %s, other: %s' % (self, other))
        return self.flight > other.flight

    def __ge__(self, other):
        print('__ge__ called - self: %s, other: %s' % (self, other))
        return self.flight >= other.flight

    def __eq__(self, other):
        print('__gt__ called - self: %s, other: %s' % (self, other))
        return self.flight == other.flight
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newName):
        self.__name = newName
    
    @name.deleter
    def name(self):
        del self.__name

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, newStatus):
        self.__status = newStatus
    
    @status.deleter
    def status(self):
        del self.__status

    @property
    def flight(self):
        return self.__flight

    @flight.setter
    def flight(self, newFlight):
        self.__flight = newFlight
    
    @flight.deleter
    def flight(self):
        del self.__flight

# Part 3.1
# ------------------------------

astronauts = []

with open('astronauts.csv', 'r') as astro:
    csv_reader = csv.DictReader(astro)
    astronauts = list(csv_reader)

astros = []

for a in astronauts:
    name = Astronaut(a['Name'],a['Status'],a['Space Flight (hr)'])
    astros.append(name)

# Part 3.2
# ------------------------------

def part3_2():
    print('\nPart 3.2')
    print('====================\n')

    print(astros[0].__dict__)

part3_2()

# Part 3.3
# ------------------------------
def part3_3():
    print('\nPart 3.3')
    print('====================\n')

    astro_1 = random.choice(astros)
    astro_2 = random.choice(astros)

    print(astro_1 > astro_2)

    astro_1 = random.choice(astros)
    astro_2 = random.choice(astros)

    print(astro_1 > astro_2)

    astro_1 = random.choice(astros)
    astro_2 = random.choice(astros)

    print(astro_1 == astro_2)

part3_3()

# Part 3.4
# ------------------------------

def part3_4():
    print('\nPart 3.4')
    print('====================\n')

    for a in astros:
        print(a)

part3_4()