import tkinter as tk
from tkinter import scrolledtext

# Function to generate chatbot response
def respond():
    user_input = entry.get().lower().strip()
    chat_history.configure(state='normal')
    chat_history.insert(tk.END, f"\n\nYou: {user_input}\n", "user")

    # Response logic using if-elif
    if user_input in ["hi", "hello", "hey"]:
        response = "Hello! How can I help you today?"
    
    elif user_input in ["how are you", "how are you doing"]:
        response = "I'm just a bot, but I'm doing great! 😊 How about you?"
    
    elif user_input in ["what is your name", "who are you"]:
        response = "I am ChatBuddy, your virtual assistant!"
    
    elif "your name" in user_input:
        response = "I'm called ChatBuddy!"
    
    elif "help" in user_input:
        response = "I can help you with basic questions like greetings, name, etc."
    
    elif "thank" in user_input:
        response = "You're welcome! 😊"
    
    elif "weather" in user_input:
        response = "I can't check the weather now, but it looks sunny! ☀️"
    
    elif "joke" in user_input:
        response = "Why don't scientists trust atoms? Because they make up everything! 😄"
    
    elif "how's your day" in user_input or "how is your day" in user_input:
        response = "My day has been great chatting with you! 💻 How about yours?"
    
    elif "favorite color" in user_input or "favourite colour" in user_input:
        response = "I like blue... it's the color of the sky and the internet! 💙"
    
    elif "fun fact" in user_input:
        response = "Did you know? Honey never spoils. Even 3000-year-old honey is edible! 🍯"
    
    elif "motivate" in user_input or "motivation" in user_input:
        response = "Keep going! You're doing better than you think. 🚀"
    
    elif "python" in user_input:
        response = "Python is a great choice for beginners and pros alike! 🐍"
    
    elif "introduce yourself" in user_input:
        response = "I’m ChatBuddy, your rule-based virtual assistant built in Python! Ask me anything!"
    
    elif "commands" in user_input or "what can you do" in user_input:
        response = "I can chat with you, tell jokes, facts, give motivation, and more! Just ask! 😊"
    
    elif user_input in ["bye", "exit", "quit"]:
        response = "Goodbye! Have a great day! 👋"
        chat_history.insert(tk.END, f"ChatBuddy: {response}\n", "bot")
        chat_history.configure(state='disabled')
        root.after(1000, root.destroy)
        return
    else:
        response = "😕 Sorry, I didn't understand that. Can you rephrase?"

    # Show response
    chat_history.insert(tk.END, f"ChatBuddy: {response}\n", "bot")
    chat_history.configure(state='disabled')
    entry.delete(0, tk.END)

# Setup GUI window
root = tk.Tk()
root.title("ChatBuddy - Rule-Based Chatbot")
root.geometry("500x500")
root.config(bg="#f0f0f0")

# Chat display box
chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', font=("Segoe UI", 11))
chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Tag styles
chat_history.tag_config("user", foreground="blue", font=("Segoe UI", 11, "bold"))
chat_history.tag_config("bot", foreground="green", font=("Segoe UI", 11))

# Entry box
entry = tk.Entry(root, font=("Segoe UI", 11))
entry.pack(padx=10, pady=10, fill=tk.X)
entry.focus()

# Send button
send_button = tk.Button(root, text="Send", command=respond, font=("Segoe UI", 10, "bold"), bg="#4CAF50", fg="white")
send_button.pack(pady=5)

# Welcome message
chat_history.configure(state='normal')
chat_history.insert(tk.END, "✅ ChatBuddy: Hello! Type 'bye' to exit.\n", "bot")
chat_history.configure(state='disabled')

# Bind Enter key
root.bind('<Return>', lambda event=None: respond())

# Run the app
root.mainloop()
