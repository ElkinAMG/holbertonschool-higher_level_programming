#!/usr/bin/python3
'''

This file has the `Base` class.

'''
import json
import turtle
import csv
from time import sleep


def fward_turtle(steps, angle):
    '''
    It draws a turtle with `height`.
    '''

    turtle.shape("turtle")
    turtle.color("green")

    turtle.right(angle)
    turtle.forward(steps)


def moves(list_shapes):
    '''
    It draws a list of shapes.
    '''

    for shape in list_shapes:
        for i in range(4):
            if i == 0:
                fward_turtle(shape.width, 0)
            if i == 1:
                fward_turtle(shape.height, -90)
            if i == 2:
                fward_turtle(shape.width, -90)
            if i == 3:
                fward_turtle(shape.height, -90)
        sleep(2)
        turtle.clearscreen()


class Base:
    '''
    This class is the `base` of all other classes
    in this project.
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
        The constructor that stablish the id.
        '''
        if not (id is None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        Returns the JSON string representation of `list_dictionaries`.
        '''

        if list_dictionaries is None:
            list_dictionaries = []

        return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        '''
        Returns the list of JSON string representation.
        '''

        rep = []

        if not (json_string is None):
            if len(json_string) > 0:
                rep = json.loads(json_string)

        return (rep)

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''
        Draws all the Rectangles and Squeares.
        '''

        turtle.title("-- RECTANGLES --")
        moves(list_rectangles)

        sleep(2)

        turtle.title("-- SQUARES --")
        moves(list_squares)

        turtle.title("END - PRESS CLICK FOR CLOSE")
        turtle.Screen().exitonclick()

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Writes `list_objs` to a file.
        '''

        objs = []
        filename = cls.__name__ + ".json"

        if not (list_objs is None):
            for i in list_objs:
                objs.append(cls.to_dictionary(i))

        with open(filename, "w") as file:
            file.write(cls.to_json_string(objs))

    @classmethod
    def create(cls, **dictionary):
        '''
        Returns an instance with all attributes already set.
        '''

        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)

        return (dummy)

    @classmethod
    def load_from_file(cls):
        '''
        Returns a list of instances.
        '''

        rep = []
        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r") as file:
                rep = cls.from_json_string(file.read())
            for a, b in enumerate(rep):
                rep[a] = cls.create(**rep[a])
        except:
            pass

        return (rep)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''
        Saves to csv file.
        '''

        filename = cls.__name__ + '.csv'

        with open(filename, 'w', newline='') as f:
            spam = csv.writer(f)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    spam.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    spam.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        '''
        Loads from csv file.
        '''

        filename = cls.__name__ + '.csv'

        objs = []

        try:
            with open(filename, 'r') as f:
                spam_reader = csv.reader(f)
                for obj in spam_reader:
                    if cls.__name__ == "Rectangle":
                        dic = {
                            'id': int(obj[0]),
                            'width': int(obj[1]),
                            'height': int(obj[2]),
                            'x': int(obj[3]),
                            'y': int(obj[4])
                        }
                    elif cls.__name__ == "Square":
                        dic = {
                            'id': int(obj[0]),
                            'size': int(obj[1]),
                            'x': int(obj[2]),
                            'y': int(obj(3))
                        }
                    dum = cls.create(**dic)
                    objs.append(dum)
        except:
            pass

        return (objs)
