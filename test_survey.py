#Can we test if users using AnonymousSurvey can
#enter more than one response?

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    #Tests the class AnonymousSurvey
    def test_store_single_response(self):
        #Testing the single response method per user
        question = "What language did you learn first?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        #Testing if a user can enter three responses
        question = "What language did you learn first?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'French', 'Spanish']
        #Loop through the list and append to response
        for response in responses:
            my_survey.store_response(response)
        #Assert each response individually via loop
        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__ == '__main__':
    unittest.main()