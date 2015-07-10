import json
from Category import Category
from Fact import Fact

__author__ = 'bill'
from flask import Flask
app = Flask(__name__)

def obj_dict(obj):
    return obj.__dict__

@app.route('/')
def hello_world():
    thing = {
        "this": "that"
    }
    return json.dumps(thing)

@app.route('/categories')
def get_categories():
    # categories = ["Category 1", "Category 2", "Category 3"]
    return json.dumps(categories, default=obj_dict)

@app.route('/facts/<int:category_id>')
def get_facts(category_id):
    facts = ["Fact 1", "Fact 2", "Fact 3"]
    return json.dumps(facts)

if __name__ == '__main__':
    category1 = Category("category 1", 1)
    category2 = Category("category 2", 2)
    category3 = Category("category 3", 3)
    categories = [category1, category2, category3]


    app.debug = True
    app.run("0.0.0.0", 10080)

