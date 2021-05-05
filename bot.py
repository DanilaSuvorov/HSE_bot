from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters
from skill import EchoSkill


class Bot:
    def __init__(self, token):
        self.token = token
        self.updater = Updater(token=self.token, use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.message_handler = MessageHandler(Filters.text & (~Filters.command), self.get_message)
        self.dispatcher.add_handler(self.message_handler)
        self.skills = []

    def get_message(self, update, context):
        message = update.message.text
        skill = EchoSkill(message, update, context)
        if skill.match():
            skill.answer()

    def run(self):
        self.updater.start_polling()