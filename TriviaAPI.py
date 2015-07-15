import os
import pickle
from Category import Category
from Fact import Fact

__author__ = 'bill'
import requests
import html
from bs4 import BeautifulSoup

div_start = "&lt;div&gt;"
div_end = "&lt;/div&gt;"
line_break = "&lt;br&gt;"


class TriviaAPI(object):
    def __init__(self, filter_file="filter.pickle"):
        self.url = "https://pareshchouhan-trivia-v1.p.mashape.com/v1/"
        self.key_string = 'Fv2O8814X8mshAn5FMHV5mAKdXEKp157nNejsnd5AzdNFZcrgZ'
        self.result_type_string = 'application/json'
        self.headers = {
            "X-Mashape-Key": self.key_string,
            "Accept": self.result_type_string
        }
        self.category_filter = pickle.load(
            open(
                os.path.join(
                    os.path.dirname(__file__),
                    filter_file
                ),
                "rb"
            )
        )

    def get_categories(self, filtered=True):
        if filtered:
            return self.get_filtered_categories()
        else:
            return self.get_unfiltered_categories()


    def get_filtered_categories(self):
        endpoint = "getCategoryList"
        query = endpoint
        results = requests.get(self.url + query, headers=self.headers)
        categories = []
        results_json = results.json()
        for result in results_json:
            category = Category(result["categ_name"], result["id"])
            if category.ID not in self.category_filter:
                categories.append(category)

        return categories



    def get_unfiltered_categories(self):
        endpoint = "getCategoryList"
        query = endpoint
        results = requests.get(self.url + query, headers=self.headers)
        categories = []
        results_json = results.json()
        for result in results_json:
            category = Category(result["categ_name"], result["id"])
            categories.append(category)

        return categories

    def get_facts_by_category(self, category_id):
        endpoint = "getQuizQuestionsByCategory"
        limit = 10
        page = 1
        # query = endpoint + "?categoryId={}&limit={}&page={}"
        query = endpoint + "?categoryId={}".format(category_id)
        results = requests.get(self.url + query, headers=self.headers)
        facts = []
        results_json = results.json()
        for result in results_json:
            question = result["q_text"]
            # question = question.replace(div_start, "")
            # question = question.replace(div_end, "")
            # question = question.replace(line_break, "")
            question = html.unescape(question)
            question = BeautifulSoup(question, "html.parser").text
            fact = Fact(question,
                        result["id"],
                        question=question,
                        category_id=result["categ_id"],
                        correct_answer_number=str(result["q_correct_option"]),
                        answers={
                            "1": result["q_options_1"],
                            "2": result["q_options_2"],
                            "3": result["q_options_3"],
                            "4": result["q_options_4"]
                        })
            # print(fact)
            facts.append(fact)
        return facts


def make_filter_pickle(trivia, file_name="filter.pickle", min_categories=1):
    categories = trivia.get_categories(filtered=False)
    # file_name = "test.pickle"
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, file_name)
    file = open(file_path, "wb")
    category_filter = set()
    for category in categories:
        facts = trivia.get_facts_by_category(category.ID)
        if len(facts) < min_categories:
            category_filter.add(category.ID)
    pickle._dump(category_filter, file)
    file.close()


if __name__ == '__main__':
    trivia = TriviaAPI()
    print(trivia.category_filter)
    # print(trivia.get_categories())
    # trivia.get_facts_by_category(12)
    # trivia.get_facts_by_category(3)
    # print(trivia.get_facts_by_category(3))
    # make_filter_pickle(trivia, min_categories=3)
    # trivia = TriviaAPI()
    # print(trivia.category_filter)
    # print("***********unfiltered:")
    # unfiltered_categories = trivia.get_categories(filtered=False)
    # for category in unfiltered_categories:
    #     print("{}, ".format(category.ID), end="")
    # print("***********filtered:")
    filtered_categories = trivia.get_categories()
    for category in filtered_categories:
        print("{} -> #{}, ".format(category.ID, len(trivia.get_facts_by_category(category.ID))))
