#import the lib used for chatbox
from nltk.chat.util import Chat, reflections

#using expressions to determine input and putput 
def chatbox_ai(): 
    patterns = [
        ['my name is (.*)', ['hi %1!']],
        ['(hi|hello|hey|yo|hola)', ['hey there', 'heyyy', 'whats good']],
        ['(.*) in (*) is fun', ['%1 in %2 is indeed fun']],
        ['(.*)(location|city)?', ['Tokyo, Japan']],
        ['(.*) created you?', ['Den did!']]
    ]
    chat = Chat(patterns, reflections)
    chat.converse()



if __name__ == "__main__":
   chatbox_ai()
