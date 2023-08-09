import telebot
import os
from dotenv import load_dotenv
import util
import RadarrApi

load_dotenv()


BotToken = os.getenv('BOT_TOKEN')
host = os.getenv("HOST")
port = os.getenv("PORT")
apikey = os.getenv("radarr_ApiKey")


radarr = RadarrApi.RadarrApi(apikey,host,port)
bot = telebot.TeleBot(BotToken, parse_mode=None)

print("Bot Started")


@bot.message_handler(commands=['test', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Test. Success")


@bot.message_handler(commands=['inlinetest'])
def start(message):
    # Create an inline keyboard
    markup = telebot.types.InlineKeyboardMarkup()

    # Add two buttons to the inline keyboard
    option1_button = telebot.types.InlineKeyboardButton(
        text="Option 1", callback_data="option1")
    option2_button = telebot.types.InlineKeyboardButton(
        text="Option 2", callback_data="option2")
    markup.add(option1_button, option2_button)

    # Send a message with the inline keyboard
    bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)


@bot.message_handler(commands=['add'])
def addMovie(message):
    bot.send_message(message.chat.id, "Please enter a title:")
    bot.register_next_step_handler(message, ask_for_option)


def ask_for_option(message):
    title = message.text
    radarr.lookup(title)
    image_urls = [
        "https://image.tmdb.org/t/p/original/QAL6ZI2mLEXiIUGhGYd1fYuj9Q.jpg",
        "https://image.tmdb.org/t/p/original/QAL6ZI2mLEXiIUGhGYd1fYuj9Q.jpg",
        "https://image.tmdb.org/t/p/original/QAL6ZI2mLEXiIUGhGYd1fYuj9Q.jpg"
    ]

    for idx, image_url in enumerate(image_urls):
        markup = telebot.types.InlineKeyboardMarkup()
        button = telebot.types.InlineKeyboardButton(
            text="Add", callback_data=f"add_image_{idx}")
        markup.add(button)
        bot.send_photo(message.chat.id, image_url,
                       caption="Image with Add button:", reply_markup=markup)
        



@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "option1":
        bot.send_message(call.message.chat.id, "You chose Option 1")
    elif call.data == "option2":
        bot.send_message(call.message.chat.id, "You chose Option 2")
    elif call.data == "done":
        bot.send_message(call.message.chat.id, "You chose Option 2")


bot.infinity_polling()
