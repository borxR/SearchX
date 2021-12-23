from telegram.ext import CommandHandler

from bot import LOGGER, dispatcher
from bot.helper.drive_utils.gdriveTools import GoogleDriveHelper
from bot.helper.ext_utils.bot_utils import new_thread
from bot.helper.telegram_helper.message_utils import sendMessage, deleteMessage
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.filters import CustomFilters

@new_thread
def deleteNode(update, context):
    LOGGER.info('User: {} [{}]'.format(update.message.from_user.first_name, update.message.from_user.id))
    args = update.message.text.split(" ", maxsplit=1)
    if len(args) > 1:
        link = args[1]
        msg = sendMessage(f"<b>Deleting:</b> <code>{link}</code>", context.bot, update)
        LOGGER.info(f"Deleting: {link}")
        gd = GoogleDriveHelper()
        result = gd.deletefile(link)
        deleteMessage(context.bot, msg)
        sendMessage(result, context.bot, update)
    else:
        sendMessage("Evidede GDrive link?,nere olla link ayak", context.bot, update)
        LOGGER.info("Deleting: None")

delete_handler = CommandHandler(BotCommands.DeleteCommand, deleteNode,
                                filters=CustomFilters.owner_filter, run_async=True)
dispatcher.add_handler(delete_handler)
