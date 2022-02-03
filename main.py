from telegram import Update
from telegram.ext import Updater , CommandHandler, CallbackQueryHandler, CallbackContext,Filters,MessageHandler
import os
from time import sleep


Token =os.environ.get("BOT_TOKEN",None)
updater = Updater( Token ,use_context = True )

def start(updater,context):
 updater.message.reply_text('''𝙷𝚊𝚒 , \n\n𝙸𝚊𝚖  𝚊  𝚂𝚒𝚖𝚙𝚕𝚎  𝚆𝚎𝚕𝚌𝚘𝚖𝚎  𝙱𝚘𝚝.  𝙰𝚍𝚍  𝚖𝚎  𝚝𝚘  𝚢𝚘𝚞𝚛  𝚐𝚛𝚘𝚞𝚙  𝚊𝚗𝚍  𝚖𝚊𝚔𝚎  𝚖𝚎  𝚊𝚜  𝚊𝚍𝚖𝚒𝚗\n\n👲 𝙼𝚊𝚒𝚗𝚝𝚊𝚒𝚗𝚎𝚍  𝙱𝚢 : @BX_Botz ''')

def help(updater,context):
 updater.message.reply_text("➠ 𝙰𝚍𝚍  𝙼𝚎  𝚃𝚘  𝙶𝚛𝚘𝚞𝚙\n\n➠ 𝙼𝚊𝚔𝚎  𝙰𝚍𝚖𝚒𝚗  𝙼𝚎\n\n👲 𝙼𝚊𝚒𝚗𝚝𝚊𝚒𝚗𝚎𝚍  𝙱𝚢 : @BX_Botz")\
 

def add_group(update: Update, context: CallbackContext):
    msg = update.message
    for member in update.message.new_chat_members:
        update.message.reply_text(f'Hai {member.full_name} , Welcome to ln Support\n\n💖Thank💖You💖For💖Joining💖')
        context.bot.deleteMessage(chat_id=msg.chat_id, message_id=msg.message_id)
        sleep(500)
        update.bot.delete_message(chat_id=msg.chat_id, message_id=msg.message_id+1)
        
add_group_handle = MessageHandler(Filters.status_update.new_chat_members, add_group)
updater.dispatcher.add_handler(add_group_handle)

dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(CommandHandler('help',help))

updater.start_polling()
updater.idle()
