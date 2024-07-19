import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk
from tkinter import scrolledtext, Button, Entry

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a simple rule based bot created by Group One. Here to help on any customer service query!",]
    ],
    [
        r"how are you?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"I am fine|i'm (.*) doing good",
        ["Great to hear that, How can I help you?",]
    ],
# Admissions and enrollment
    [
        r"when does enrollment start?| when is enrollment?|when is admission?",
        ["the next enrollment begins at the beginning of September",]
    ],
    [
        r"how many times can one enroll in a year?",
        ["Three times. In January, May and September",]
    ],
    [
        r"What are the requirements (.*)",
        ["You need national identification, a high school exam certificate and a good medical report",]
    ],
# What courses are available?
    [
        r"what courses are available?",
        ["please check the website for more information",]
    ],
    [
        r"Do you have (.*) course?|is (.*) available?",
        ["Please check the website",]
    ],
    [
        r"when is the application deadline?",
        ["The application deadline is 2 weeks after the opening date",]
    ],
#Campus
    [
        r"where is the campus?",
        ["The two campuses are located in Langata and Gaba. We also offer fully online classes",]
    ],
    [
        r"what is the operating time?",
        ["The school is open from 8 am to 5 pm on weekdays and closed on weekends.",]
    ],
]


class ChatWindow:
    def __init__(self, master):
        self.master = master
        master.title("Simple Chatbot")

        self.chatbot = Chat(pairs, reflections)

        self.chat_history = scrolledtext.ScrolledText(master, width=50, height=20)
        self.chat_history.pack(pady=10)

        self.user_input = Entry(master, width=50)
        self.user_input.pack(pady=10)
        self.user_input.bind('<Return>', self.handle_enter)

        self.send_button = Button(master, text="Send", command=self.send_message)
        self.send_button.pack()

        self.initialize_chat()

    def initialize_chat(self):
        self.update_chat_history("Bot: Hi! I am a simple rule-based chatbot created by Group One. How can I help you today? Type 'quit' to exit.")

    def handle_enter(self, event):
        self.send_message()

    def send_message(self):
        user_query = self.user_input.get()
        if user_query.strip() == '':
            return

        self.user_input.delete(0, tk.END)
        self.update_chat_history(f"You: {user_query}")

        if user_query.lower() == 'quit':
            self.update_chat_history("Bot: Goodbye!")
            self.master.after(2000, self.master.destroy)  # Close window after 2 seconds
            return

        response = self.chatbot.respond(user_query)
        if response:
            self.update_chat_history(f"Bot: {response}")
        else:
            self.update_chat_history("Bot: I'm sorry, I didn't understand that. Please try again.")

    def update_chat_history(self, message):
        self.chat_history.configure(state='normal')
        self.chat_history.insert(tk.END, message + '\n')
        self.chat_history.configure(state='disabled')
        self.chat_history.yview(tk.END)

def main():
    root = tk.Tk()
    chat_window = ChatWindow(root)
    root.mainloop()

# initiating the conversation
if __name__ == "__main__":
    main()