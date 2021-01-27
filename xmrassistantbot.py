import telebot
from telebot import types

token = ''
bot = telebot.TeleBot(token, parse_mode='Markdown')


@bot.message_handler(commands=['start'])

def first_step(message):
    main_key = types.ReplyKeyboardMarkup(resize_keyboard=True)
    main_key.row('Internet Services 🌍', 'Crypto Services 🏴‍☠️')
    main_key.row('Resources 📖', 'Contact 📩')
    msg = bot.send_message(message.chat.id, 'Choose from the following list:', reply_markup=main_key)
    bot.register_next_step_handler(msg, second_step)

def second_step(message):
    sub_key = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == '/start':
        first_step(message)
        return
    else:
        if message.text == 'Internet Services 🌍':
            sub_key.row('VPS', 'VPN')
            sub_key.row('Email', 'Proxy')
            sub_key.row('VoIP', 'Other Internet Services')
        elif message.text == 'Crypto Services 🏴‍☠️':
            sub_key.row('Exchange', 'Wallet')
            sub_key.row('Payment Gateway', 'Other Crypto Services')
        elif message.text == 'Resources 📖':
            with open('services/resources.txt') as f:
                resources_list = f.read()
                bot.send_message(message.chat.id, resources_list, disable_web_page_preview=True)
                first_step(message)
                return
        elif message.text == 'Contact 📩':
            bot.send_message(message.chat.id, 'Your contact')
            first_step(message)
            return
    sub_key.row('Main Menu 🔙')
    msg = bot.send_message(message.chat.id, 'Which service?', reply_markup=sub_key)
    bot.register_next_step_handler(msg, third_step)

def third_step(message):
    if message.text == '/start' or message.text == 'Main Menu 🔙':
        first_step(message)
        return
    else:
        if message.text == 'VPS':
            with open('services/internet_services/vps.txt') as f:
                vps_list = f.read()
                bot.send_message(message.chat.id, vps_list, disable_web_page_preview=True)
        elif message.text == 'VPN':
            with open('services/internet_services/vpn.txt') as f:
                vpn_list = f.read()
                bot.send_message(message.chat.id, vpn_list, disable_web_page_preview=True)
        elif message.text == 'Email':
            with open('services/internet_services/email.txt') as f:
                email_list = f.read()
                bot.send_message(message.chat.id, email_list, disable_web_page_preview=True)
        elif message.text == 'Proxy':
            with open('services/internet_services/proxy.txt') as f:
                proxy_list = f.read()
                bot.send_message(message.chat.id, proxy_list, disable_web_page_preview=True)
        elif message.text == 'VoIP':
            with open('services/internet_services/voip.txt') as f:
                voip_list = f.read()
                bot.send_message(message.chat.id, voip_list, disable_web_page_preview=True)
        elif message.text == 'Other Internet Services':
            with open('services/internet_services/other_internet_services.txt') as f:
                other_list = f.read()
                bot.send_message(message.chat.id, other_list, disable_web_page_preview=True)
        elif message.text == 'Exchange':
            with open('services/crypto_services/exchange.txt') as f:
                exchange_list = f.read()
                bot.send_message(message.chat.id, exchange_list, disable_web_page_preview=True)
        elif message.text == 'Wallet':
            with open('services/crypto_services/wallet.txt') as f:
                wallets_list = f.read()
                bot.send_message(message.chat.id, wallets_list, disable_web_page_preview=True)
        elif message.text == 'Payment Gateway':
            with open('services/crypto_services/payment_gateway.txt') as f:
                gateways_list = f.read()
                bot.send_message(message.chat.id, gateways_list, disable_web_page_preview=True)
        elif message.text == 'Other Crypto Services':
            with open('services/crypto_services/other_crypto_services.txt') as f:
                other2_list = f.read()
                bot.send_message(message.chat.id, other2_list, disable_web_page_preview=True)

    msg = bot.send_message(message.chat.id, 'Choose another service or return:')
    bot.register_next_step_handler(msg, fourth_step)

def fourth_step(message):
    third_step(message)
    return

if __name__ == "__main__":
    bot.polling(none_stop=True)
