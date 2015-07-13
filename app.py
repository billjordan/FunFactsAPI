import json
from Category import Category
from Fact import Fact
from TriviaAPI import TriviaAPI

__author__ = 'bill'
from flask import Flask
app = Flask(__name__)

def obj_dict(obj):
    return obj.__dict__

@app.route('/')
def hello_world():
    return "Fun Facts API"

@app.route('/categories')
def get_categories():
    # categories = ["Category 1", "Category 2", "Category 3"]
    # return list of dicts ensure order by sorting
    categories = {"categories": trivia_api.get_categories()}
    return json.dumps(categories, default=obj_dict, sort_keys=True)

@app.route('/facts/<int:category_id>')
def get_facts(category_id):
    # facts = ["Fact 1", "Fact 2", "Fact 3"]
    # return list of dicts ensure order by sorting
    facts = {"facts": trivia_api.get_facts_by_category(category_id)}
    return json.dumps(facts, default=obj_dict, sort_keys=True)

if __name__ == '__main__':
    # category1 = Category("API category 1", 1)
    # category2 = Category("API category 2", 2)
    # category3 = Category("API category 3", 3)
    # categories = [category1, category2, category3]
    # fact1 = Fact("API Fact 1", 1)
    # fact2 = Fact("API Fact 2", 2)
    # fact3 = Fact("API Fact 3", 3)
    # facts = [fact1, fact2, fact3]

    trivia_api = TriviaAPI()
    app.debug = True
    app.run("0.0.0.0", 10080)

