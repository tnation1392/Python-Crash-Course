#import the class in
from survey import AnonymousSurvey

#Define a question and make the survey
question = "What language did you first learn?"
survey1 = AnonymousSurvey(question)

#Display the question and store responses
survey1.show_question()
print("Enter q to quit")
while True:
    response = input("Language: ")
    if response == "q":
        break
    survey1.store_response(response)

#Show the results
print("\nThank you for your responses!")
survey1.show_results()