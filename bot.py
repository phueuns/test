import telebot
import requests 
#tele:@htmliq
bot = telebot.TeleBot("826692824:AAHwkYnUtmJoxNxprPoO9wYXWJTLc7VsbvY")

@bot.message_handler(commands=['start'])
def ss(message):
    url_0 = requests.get(f"https://tzzzzava.xyz/Apis/EUR-TO-IQD-API/Biticoin.php").json()
    ll_0 = url_0['result']['Bitcoin'] 

    
    bot.reply_to(message,f"{ll_0}")
    




bot.polling(True)
#tele:@htmliq
