#library
from transformers import pipeline

#question-answering tasks by passing "question-answering" as an argument to the pipeline() function.
qn_pipeline = pipeline("question-answering")

#This block of code prompts the user to input a question, which will be used to query the context provided in the QN_input dictionary.
#QN_input dictionary contains two keys: "question" and "context".
#The "question" key takes the user input, while the "context" key provides the context to be searched for an answer.

QN_input = {
    'question':input("Question: "),
    'context':"John Fitzgerald Kennedy, often referred to by his initials JFK and the nickname Jack, was an American Politician who served as the 35th president of the United States."
    }

#uses the pipeline object to process the question and context in the QN_input dictionary and returns a 
#dictionary containing the predicted answer to the question.
res = qn_pipeline(QN_input)

#prints the predicted answer.
print("Answer: ",res['answer'])