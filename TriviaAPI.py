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
    def __init__(self):
        self.url = "https://pareshchouhan-trivia-v1.p.mashape.com/v1/"
        self.key_string = 'Fv2O8814X8mshAn5FMHV5mAKdXEKp157nNejsnd5AzdNFZcrgZ'
        self.result_type_string = 'application/json'
        self.headers = {
            "X-Mashape-Key": self.key_string,
            "Accept": self.result_type_string
        }

    def get_categories(self):
        endpoint = "getCategoryList"
        query = endpoint
        results = requests.get(self.url + query, headers = self.headers)
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
                        correct_answer_number = str(result["q_correct_option"]),
                        answers = {
                            "1": result["q_options_1"],
                            "2": result["q_options_2"],
                            "3": result["q_options_3"],
                            "4": result["q_options_4"]
                        })
            print(fact)
            facts.append(fact)
        return facts



if __name__ == '__main__':
    trivia = TriviaAPI()
    # print(trivia.get_categories())
    # trivia.get_facts_by_category(12)
    trivia.get_facts_by_category(3)
    # print(trivia.get_facts_by_category(3))
