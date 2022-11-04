from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

class Chat_T:
    chatbot: None

    def __init__(self):
        self.chatbot = ChatBot("ChatBot")
    # Training with Personal Ques & Ans
        conversation = [
            "Hello",
            "Hi there!",
            "How are you doing?",
            "I'm doing great.",
            "You're welcome.",
            "who Developed you",
            "NLP class"
        ]
        trainer = ListTrainer(self.chatbot)
        trainer.train(conversation)

        additional_training = [
            "Who are you?",
            "Hi, can you tell me what your name is?",
            "I have a question.",
            "Please, explain your concern.",
            "What is today's weather?",
            "I am not sure where you are located, but everything is clear here.",
            "Ok",
            "Is there anything else I can help you with?",
            "No.",
            "If that is all, have a nice day.",
            "What is NLP?",
            "Only the BEST THING EVER! Well, in my opinion.",
            "Who cares?",
            "I'm sure many people care. So do I. How can I help?",
            "Get lost.",
            "Ok, sorry I couldn't help more."
        ]

        trainer.train(additional_training)

    def chat(self, t1):
        response = self.chatbot.get_response(t1)
        return response