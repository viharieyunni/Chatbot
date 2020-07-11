from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('Rachel')

    #Training the chat bot

convo = [
    'Hi',
    'Hello',
    'What is your name?',
    'My name is Rachel',
    'Which country are you from?',
    'I am from India',
    'Do you like the show Friends?',
    'Yes, ofcourse. Do you?',
    'I Do.',
    'Who is your favourite character?',
    'Chandler',
    'Could that be any more right?'
]

trainer = ListTrainer(chatbot)
trainer.train(convo)

#Testing the chatbot with single answer
#answer = chatbot.get_response('Which country are you from?')
#print(answer)

#Testing with mutliple answers
print("Talk to bot")
while True:
    query=input()
    if query == 'exit':
        break
    else:
        answer = chatbot.get_response(query)
        print("Rachel:",answer)

