__author__ = 'bill'
from json import JSONEncoder

class Category(JSONEncoder):
    def __init__(self, label, ID):
        self.label = label
        self.ID = ID

    def __str__(self):
        return "ID:{}\t{}".format(self.ID, self.label)


