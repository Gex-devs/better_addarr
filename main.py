import telebot
import os
from dotenv import load_dotenv


load_dotenv()


BotToken = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(BotToken, parse_mode=None)

print("Bot Started")

@bot.message_handler(commands=['test', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Test. Success")



bot.infinity_polling()