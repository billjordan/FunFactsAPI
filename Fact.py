__author__ = 'bill'


class Fact(object):
    def __init__(self, label, ID, question = "", answers = {}, correct_answer_number = None, category_id = ""):
        self.label = label
        self.ID = ID
        self.question = question
        self.answers = answers
        self.correct_answer_number = correct_answer_number
        self.category_id = category_id

    def __str__(self):
        returnStr = "Label: {}\nID: {}\nCategory_id: {}\nQuestion: {}\n".format(self.label,
                                                                           self.ID,
                                                                           self.category_id,
                                                                           self.question)
        for answer_number in sorted(self.answers.keys()):
            returnStr += "\n\t{}) {}".format(answer_number, self.answers[answer_number])
        returnStr += "\n\nCorrect answer: {}".format(self.answers[self.correct_answer_number])
        return returnStr