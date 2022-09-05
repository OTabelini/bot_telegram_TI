import telebot


# You can get this key from @BotFather on Telegram
api_key = "xxxxxxxxxxxxx"

# Here is the command that the bot are created 
bot = telebot.TeleBot(api_key)

# Always put message_handler and a option together.
@bot.message_handler(commands=["option1"])
def option1(message):
    bot.send_message(message.chat.id, 
    """
RESUME ABOUT YOUR EDUCATION
    """
    )

@bot.message_handler(commands=["option2"])
def option2(message):
    bot.send_message(message.chat.id, 
    """
SUMMARY OF SKILLS!!!!!!!!!!

> aaaaaaaa;
> bbbbbbbb;
> cccccccc;
> dddddddd;
> eeeeeeee;
> ffffffff;
> gggggggg;

etc.
    """
    )

@bot.message_handler(commands=["option3"])
def option3(message):
    bot.send_message(message.chat.id, "Age and localization")

@bot.message_handler(commands=["option4"])
def option4(message):
    bot.send_message(message.chat.id,
    """
LinkedIn:
Email:
Cel:
    """
    )

@bot.message_handler(commands=["option5"])
def option5(message):
    # print(message)
    bot.send_message(message.chat.id, 
    """
    > Link: https://github.com/USER
    """
    )

@bot.message_handler(commands=["option6"])
def option6(message):
    # print(message)
    bot.send_message(message.chat.id, 
    """
You can put here the link from (drive or any cloud storage) your cv.
    """
    )

def check(message):
    return True

@bot.message_handler(func=check)
def reply(message):
    text = f"""
    Hello {message.from_user.first_name}, welcome!
    I'm bot XXXXXXX!
    
    Choose one option to continue (click in one of them):

    /option1 Education               (EXAMPLE)
    /option2 Summary of Skills       (EXAMPLE)
    /option3 Age and Localization    (EXAMPLE)
    /option4 Contact                 (EXAMPLE)
    /option5 GitHub                  (EXAMPLE)
    /option6 Resumee - CV            (EXAMPLE)
    
Please, select one option above to proceed the information.
 
"""
    bot.send_message(message.chat.id, text) 

# This function are responsable to make the bot responsivem check that and other functions that I use here in the documentation of telebot!
bot.polling()
 