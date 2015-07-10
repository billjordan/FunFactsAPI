__author__ = 'bill'
from json import JSONEncoder

class Category(JSONEncoder):
    def __init__(self, label, ID):
        self.label = label
        self.ID = ID




