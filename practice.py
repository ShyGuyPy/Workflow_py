#stepping through an interesting marshmallow tutorial
#https://www.youtube.com/watch?v=S7Fh5XnuhPU

from marshmallow import Schema, fields, pprint, post_load

class Player(object):
    def __init__(self, name, level, my_class):
        self.name = name
        self.level = level
        self.my_class = my_class

    def __repr__(self):
        return '{} is a level {} {}'.format(self.name, self.level, self.my_class)

class PlayerSchema(Schema):
    name = fields.String()
    level = fields.Integer()
    my_class = fields.String()

    #this automatically instantiates the Player class
    @post_load
    def create_player(self,data):
        return Player(**data)
        #this is same as 'return Player(name, level, my_class)

input_dict= {}

input_dict['name'] = input("Name thyself: ")
input_dict['level'] = input("what level have you achieved...be honest: ")
input_dict['my_class'] = input("What is your class?: ")

#the_player = Player(name=input_dict['name'], level=input_dict['level'], my_class=input_dict['class'])

schema = PlayerSchema()
#result = schema.dump(the_player)
result = schema.load(input_dict)

pprint(result.data)
pprint(input_dict['my_class'])
#pprint(the_player)