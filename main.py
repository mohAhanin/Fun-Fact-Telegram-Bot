import telebot
import random

bot = telebot.TeleBot('token id')

# List of random facts
facts = [
    "Honey never spoils.",
    "A day on Venus is longer than a year on Venus.",
    "Bananas are berries, but strawberries aren't.",
    "There are more stars in the universe than grains of sand on Earth."
     "Honey never spoils.",
    "A day on Venus is longer than a year on Venus.",
    "Bananas are berries, but strawberries aren't.",
    "There are more stars in the universe than grains of sand on Earth.",
    "Octopuses have three hearts.",
    "A group of flamingos is called a 'flamboyance'.",
    "The shortest war in history lasted 38 minutes.",
    "A single strand of spaghetti is called a 'spaghetto'.",
    "The Eiffel Tower can be 15 cm taller during the summer.",
    "Wombat poop is cube-shaped."
]

# Dictionary to keep track of users who want more facts.
user_states = {}

# Handles all text messages that contain the commands '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.reply_to(message, "Hi! I'm your Random Facts Bot. Type /fact to get a random fact.")

# Handles the /fact command to send a random fact
@bot.message_handler(commands=['fact'])
def send_random_fact(message):
    user_states[message.from_user.id] = True  # Set the user state to True
    random_fact = random.choice(facts)
    bot.reply_to(message, f"{random_fact}\n\nDo you want another fact? (Type 'yes' to continue or 'no' to stop.)")

# Handles the user's response for wanting more facts
@bot.message_handler(func=lambda message: message.from_user.id in user_states)
def handle_continue_fact(message):
    if message.text.lower() == 'yes':
        random_fact = random.choice(facts)
        bot.reply_to(message, f"{random_fact}\n\nDo you want another fact? (Type 'yes' to continue or 'no' to stop.)")
    elif message.text.lower() == 'no':
        bot.reply_to(message, "Okay! If you want more facts, just type /fact.")
        del user_states[message.from_user.id]  # Remove the user from the state tracking
    else:
        bot.reply_to(message, "Please type 'yes' to continue or 'no' to stop.")

# Handles all sent documents and audio files
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    if message.audio:
        bot.reply_to(message, "Please don't send audio files.")
    elif message.document:
        bot.reply_to(message, "Please don't send documents.")

# Handles all text messages that match the regular expression
@bot.message_handler(regexp="2024")
def handle_message(message):
    bot.reply_to(message, "This message contains 2024")

# Start polling
bot.polling()